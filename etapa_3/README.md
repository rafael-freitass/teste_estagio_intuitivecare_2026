# 📊 Etapa 3 – Banco de Dados e Análise (PostgreSQL)

---

## 📌 Visão Geral

Esta etapa implementa a **modelagem, carga e análise dos dados** utilizando PostgreSQL, conforme solicitado no Teste Técnico.

---

## 📦 Tecnologias

* PostgreSQL 15
* Docker / Docker Compose
* DBeaver (cliente SQL)

---

## 📁 Estrutura

```
etapa_3/
  ├── docker-compose.yml  
  ├── data/ -> Arquivos CSV utilizados  
  └── sql/
      ├── 01_ddl.sql -> Criação das tabelas
      ├── 02_import.sql -> Importação dos CSVs
      └── 03_queries_analiticas.sql -> Queries finais
```

---

## ▶️ Como Executar

### 1️⃣ Subir o banco

```
docker compose up -d
```

---

### 2️⃣ Conectar no banco

| Parâmetro | Valor      |
| --------- | ---------- |
| Host      | localhost  |
| Porta     | 5432       |
| Database  | teste_db   |
| Usuário   | teste_user |
| Senha     | teste_pass |

---

### 3️⃣ Executar os scripts na ordem

```
sql/01_ddl.sql
sql/02_import.sql
sql/03_queries_analiticas.sql
```

---

# 🧠 Decisões Técnicas

---

## 📐 Tabelas Criadas

### 🏥 operadoras

Armazena dados cadastrais das operadoras de planos de saúde.

### 💰 despesas_consolidadas

Armazena despesas trimestrais por operadora.

### 📊 despesas_agregadas

Armazena métricas estatísticas já agregadas por operadora.

---

## 🔑 Chaves Primárias e Relacionamentos

### Chaves Primárias

* operadoras.reg_ans
* despesas_consolidadas.id
* despesas_agregadas.id

### Chaves Estrangeiras

* despesas_consolidadas.reg_ans → operadoras.reg_ans

---

## ⚡ Índices Criados

* operadoras(uf)
* operadoras(razao_social)
* despesas_consolidadas(reg_ans)
* despesas_consolidadas(ano, trimestre)
* despesas_agregadas(razao_social)
* despesas_agregadas(uf)

### Justificativa

Os índices foram criados considerando os principais padrões de acesso das consultas analíticas, priorizando colunas utilizadas em filtros, agrupamentos e JOINs, reduzindo custo de varredura e melhorando performance geral.

---

# 🔄 Trade-off Técnico – Normalização

## ✔ Abordagem escolhida: Modelo Normalizado

### 📊 Volume de dados esperado

O conjunto de despesas apresenta alto volume de registros ao longo dos períodos analisados.

A normalização evita repetição de dados cadastrais, reduz consumo de armazenamento e melhora performance de escrita.

---

### 🔄 Frequência de atualizações

* Dados cadastrais possuem baixa frequência de alteração
* Dados de despesas são inseridos periodicamente

Separar essas entidades reduz inconsistências e facilita manutenção.

---

### 📈 Complexidade das queries analíticas

Embora a normalização exija JOINs, o relacionamento é simples e baseado em chave primária indexada, mantendo boa performance analítica.

---

# 💰 Trade-off Técnico – Tipos de Dados

## 💵 Valores Monetários

### Tipo escolhido

```
DECIMAL(15,2)
```

### Justificativa

* Mantém precisão financeira
* Evita erros de arredondamento presentes em FLOAT
* Facilita leitura e manutenção em comparação ao uso de centavos com INTEGER

---

## 📅 Datas e Períodos

### Tipos escolhidos

* Ano → SMALLINT
* Trimestre → SMALLINT
* Datas cadastrais → DATE

### Justificativa

* Permite validação automática do banco
* Melhor performance em filtros e agregações
* Evita inconsistências que ocorreriam com VARCHAR
* TIMESTAMP não foi utilizado pois não há necessidade de granularidade temporal

---

# ⚠️ Tratamento de Inconsistências Durante Importação

A carga dos dados foi realizada utilizando tabelas staging intermediárias, permitindo validação e limpeza antes da inserção nas tabelas finais.

---

## ❌ Valores NULL em Campos Obrigatórios

### Estratégia adotada

Registros com chaves obrigatórias ausentes foram descartados.

### Justificativa

Preserva integridade referencial e evita registros inconsistentes.

---

## 🔢 Strings em Campos Numéricos

### Estratégia adotada

Foram aplicadas funções de limpeza e conversão explícita.

### Exemplos

* Remoção de caracteres não numéricos em CNPJ
* Conversão de separadores decimais

### Justificativa

Arquivos CSV podem conter formatações regionais ou inconsistentes.

---

## 📅 Datas em Formatos Inconsistentes

### Estratégia adotada

Conversão explícita para DATE utilizando cast seguro e tratamento de valores vazios.

### Justificativa

Padroniza formato temporal e evita falhas na carga.

---

## 🔗 Integridade Referencial

Durante a carga das despesas, foram encontrados registros com operadoras inexistentes no cadastro.

### Estratégia adotada

Registros foram inseridos apenas quando havia correspondência válida na tabela dimensional operadoras.

### Justificativa

A rejeição de registros sem correspondência evita violação de integridade referencial e garante consistência entre fatos e dimensões.

---

# 🌐 Encoding dos Arquivos

Os arquivos CSV foram importados utilizando encoding UTF-8, garantindo compatibilidade com caracteres especiais presentes nos dados cadastrais.

---

# 🧹 Gerenciamento das Tabelas Staging

As tabelas staging foram utilizadas como camada intermediária para validação e limpeza dos dados.

Após a carga nas tabelas finais, foram removidas para evitar acúmulo desnecessário de dados temporários e reduzir complexidade operacional.

```
DROP TABLE staging_operadoras;
DROP TABLE staging_despesas_consolidadas;
DROP TABLE staging_despesas_agregadas;
```

---

# 📊 3.4 – Consultas Analíticas

---

## Query 1 – Top 5 Operadoras com Maior Crescimento Percentual de Despesas

### Objetivo

Identificar as operadoras com maior crescimento percentual entre o primeiro e o último trimestre analisado.

### Estratégia

* Identificar o primeiro e último período disponível por operadora
* Calcular variação percentual entre os valores
* Ordenar pelos maiores crescimentos

### Tratamento de Operadoras sem Dados em Todos os Trimestres

Operadoras que não possuem dados no primeiro ou último trimestre global podem distorcer a análise. Para evitar inconsistências, a query considera apenas operadoras com valores válidos nos períodos inicial e final analisados.

---

## Query 2 – Distribuição de Despesas por UF

### Objetivo

Identificar os 5 estados com maior volume total de despesas e calcular a média de despesas por operadora em cada UF.

### Estratégia

* Relacionar despesas com dados cadastrais das operadoras
* Agregar valores por UF
* Calcular média por operadora distinta

---

## Query 3 – Operadoras com Despesas Acima da Média Geral em Pelo Menos 2 Trimestres

### Objetivo

Identificar quantas operadoras apresentaram despesas acima da média geral em pelo menos dois trimestres analisados.

### Estratégia Adotada

Foi utilizada uma abordagem baseada em CTEs para:

1. Calcular a média global de despesas por trimestre
2. Comparar despesas individuais com essa média
3. Contabilizar quantos trimestres cada operadora superou a média

### Trade-off Técnico

A utilização de CTEs melhora legibilidade e manutenção do código, permitindo separar etapas lógicas da análise.

Embora subqueries aninhadas pudessem reduzir etapas intermediárias, a abordagem adotada favorece clareza e facilita futuras modificações, com impacto mínimo de performance devido ao uso de agregações indexadas.

---

# 🚀 Performance e Escalabilidade

A modelagem foi projetada buscando equilíbrio entre normalização e eficiência analítica.

Principais estratégias aplicadas:

* Índices em colunas utilizadas em filtros e JOINs
* Uso de tipos numéricos apropriados
* Estrutura preparada para crescimento temporal dos dados

---

# 🔎 Validação dos Resultados

Os resultados das consultas foram avaliados quanto à coerência estatística e consistência com o comportamento esperado dos dados analisados.

---

# ✅ Conclusão

A Etapa 3 implementa um pipeline completo de modelagem, carga e análise de dados utilizando PostgreSQL, seguindo boas práticas de engenharia de dados.

A solução priorizou:

* Integridade e consistência dos dados
* Clareza e manutenibilidade do modelo
* Performance analítica
* Robustez no tratamento de inconsistências

O modelo proposto permite expansão futura do volume de dados e adaptação para novos cenários analíticos sem necessidade de refatorações estruturais relevantes.

---