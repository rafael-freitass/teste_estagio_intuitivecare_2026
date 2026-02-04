-- Operadoras
CREATE TABLE staging_operadoras (
    reg_ans TEXT,
    cnpj TEXT,
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf TEXT,
    cep TEXT,
    ddd TEXT,
    telefone TEXT,
    fax TEXT,
    endereco_eletronico TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_comercializacao TEXT,
    data_registro_ans TEXT
);

COPY staging_operadoras
FROM '/data/Relatorio_cadop.csv'
WITH (
    FORMAT csv,
    DELIMITER ';',
    HEADER true,
    ENCODING 'UTF8',
    QUOTE '"'
);

INSERT INTO operadoras
SELECT
    NULLIF(reg_ans, '')::INTEGER,
    REGEXP_REPLACE(cnpj, '\D', '', 'g'),
    razao_social,
    nome_fantasia,
    modalidade,
    logradouro,
    numero,
    complemento,
    bairro,
    cidade,
    uf,
    REGEXP_REPLACE(cep, '\D', '', 'g'),
    ddd,
    telefone,
    fax,
    endereco_eletronico,
    representante,
    cargo_representante,
    NULLIF(regiao_comercializacao, '')::INTEGER,
    NULLIF(data_registro_ans, '')::DATE
FROM staging_operadoras
WHERE reg_ans IS NOT NULL;

-- Desoesas Consolidadas
CREATE TABLE staging_despesas_consolidadas (
    reg_ans TEXT,
    cnpj TEXT,
    razao_social TEXT,
    trimestre TEXT,
    ano TEXT,
    valor_despesas TEXT
);

COPY staging_despesas_consolidadas
FROM '/data/consolidado_despesas.csv'
WITH (
    FORMAT csv,
    HEADER true,
    ENCODING 'UTF8'
);

INSERT INTO despesas_consolidadas (
    reg_ans,
    trimestre,
    ano,
    valor_despesas
)
SELECT
    reg_ans::INTEGER,
    trimestre::SMALLINT,
    ano::SMALLINT,
    REPLACE(valor_despesas, ',', '.')::DECIMAL(15,2)
FROM staging_despesas_consolidadas
WHERE reg_ans IS NOT NULL
AND valor_despesas IS NOT NULL;

-- Despesas Agregadas
CREATE TABLE staging_despesas_agregadas (
    razao_social TEXT,
    uf TEXT,
    total_despesas TEXT,
    media_trimestral TEXT,
    desvio_padrao TEXT
);

COPY staging_despesas_agregadas
FROM '/data/despesas_agregadas.csv'
WITH (
    FORMAT csv,
    HEADER true,
    ENCODING 'UTF8'
);

INSERT INTO despesas_agregadas (
    razao_social,
    uf,
    total_despesas,
    media_trimestral,
    desvio_padrao
)
SELECT
    razao_social,
    uf,
    REPLACE(total_despesas, ',', '.')::DECIMAL(18,2),
    REPLACE(media_trimestral, ',', '.')::DECIMAL(18,2),
    REPLACE(desvio_padrao, ',', '.')::DECIMAL(18,2)
FROM staging_despesas_agregadas;

DROP TABLE staging_operadoras;
DROP TABLE staging_despesas_consolidadas;
DROP TABLE staging_despesas_agregadas;