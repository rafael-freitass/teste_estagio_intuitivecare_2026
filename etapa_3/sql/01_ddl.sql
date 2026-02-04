-- TABELA: OPERADORAS
CREATE TABLE operadoras (
    reg_ans INTEGER PRIMARY KEY,
    cnpj VARCHAR(14) NOT NULL UNIQUE,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(150),
    cidade VARCHAR(150),
    uf CHAR(2),
    cep VARCHAR(8),
    ddd VARCHAR(3),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(150),
    regiao_comercializacao INTEGER,
    data_registro_ans DATE
);

CREATE INDEX idx_operadoras_razao_social
ON operadoras (razao_social);

CREATE INDEX idx_operadoras_uf
ON operadoras (uf);

-- TABELA: DESPESAS CONSOLIDADAS
CREATE TABLE despesas_consolidadas (
    id BIGSERIAL PRIMARY KEY,
    reg_ans INTEGER NOT NULL,
    trimestre SMALLINT NOT NULL,
    ano SMALLINT NOT NULL,
    valor_despesas DECIMAL(15,2) NOT NULL,

    CONSTRAINT fk_operadora
        FOREIGN KEY (reg_ans)
        REFERENCES operadoras(reg_ans)
);

CREATE INDEX idx_despesas_reg_ans
ON despesas_consolidadas (reg_ans);

CREATE INDEX idx_despesas_periodo
ON despesas_consolidadas (ano, trimestre);

-- TABELA: DESPESAS AGREGADAS
CREATE TABLE despesas_agregadas (
    id BIGSERIAL PRIMARY KEY,
    razao_social VARCHAR(255) NOT NULL,
    uf CHAR(2),
    total_despesas DECIMAL(18,2),
    media_trimestral DECIMAL(18,2),
    desvio_padrao DECIMAL(18,2)
);

CREATE INDEX idx_agregadas_razao_social
ON despesas_agregadas (razao_social);

CREATE INDEX idx_agregadas_uf
ON despesas_agregadas (uf);