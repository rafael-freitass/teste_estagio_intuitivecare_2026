-- 5 operadoras com maior crescimento percentual de despesas entre o primeiro e último trimestre analisado
WITH limites_periodo AS (
    SELECT
        MIN((ano * 10 + trimestre)) AS primeiro_periodo,
        MAX((ano * 10 + trimestre)) AS ultimo_periodo
    FROM despesas_consolidadas
),

despesas_por_periodo AS (
    SELECT
        dc.reg_ans,
        o.razao_social,
        (dc.ano * 10 + dc.trimestre) AS periodo,
        SUM(dc.valor_despesas) AS total_despesas
    FROM despesas_consolidadas dc
    JOIN operadoras o ON o.reg_ans = dc.reg_ans
    GROUP BY dc.reg_ans, o.razao_social, periodo
),

crescimento AS (
    SELECT
        d1.reg_ans,
        d1.razao_social,
        d1.total_despesas AS despesa_inicial,
        d2.total_despesas AS despesa_final,
        ((d2.total_despesas - d1.total_despesas) / d1.total_despesas) * 100 AS crescimento_percentual
    FROM despesas_por_periodo d1
    JOIN despesas_por_periodo d2
        ON d1.reg_ans = d2.reg_ans
    CROSS JOIN limites_periodo lp
    WHERE d1.periodo = lp.primeiro_periodo
    AND d2.periodo = lp.ultimo_periodo
    AND d1.total_despesas > 0
)

SELECT *
FROM crescimento
ORDER BY crescimento_percentual DESC
LIMIT 5;

-- Distribuição de despesas por UF + média por operadora
WITH despesas_uf AS (
    SELECT
        o.uf,
        dc.reg_ans,
        SUM(dc.valor_despesas) AS total_operadora
    FROM despesas_consolidadas dc
    JOIN operadoras o ON o.reg_ans = dc.reg_ans
    GROUP BY o.uf, dc.reg_ans
),

agregado_uf AS (
    SELECT
        uf,
        SUM(total_operadora) AS total_despesas,
        AVG(total_operadora) AS media_por_operadora
    FROM despesas_uf
    GROUP BY uf
)

SELECT *
FROM agregado_uf
ORDER BY total_despesas DESC
LIMIT 5;

-- Operadoras acima da média geral em pelo menos 2 dos 3 trimestres analisados
WITH media_global AS (
    SELECT AVG(valor_despesas) AS media_geral
    FROM despesas_consolidadas
),

despesas_trimestre AS (
    SELECT
        reg_ans,
        ano,
        trimestre,
        SUM(valor_despesas) AS total_trimestre
    FROM despesas_consolidadas
    GROUP BY reg_ans, ano, trimestre
),

comparacao AS (
    SELECT
        dt.reg_ans,
        dt.total_trimestre,
        mg.media_geral,
        CASE
            WHEN dt.total_trimestre > mg.media_geral THEN 1
            ELSE 0
        END AS acima_media
    FROM despesas_trimestre dt
    CROSS JOIN media_global mg
),

contagem AS (
    SELECT
        reg_ans,
        SUM(acima_media) AS trimestres_acima
    FROM comparacao
    GROUP BY reg_ans
)

SELECT COUNT(*)
FROM contagem
WHERE trimestres_acima >= 2;