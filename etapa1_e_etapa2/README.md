# Teste Técnico – Estágio Intuitive Care 2026

## Visão Geral

Este projeto implementa uma **pipeline de dados em Python** para **consumir, processar e analisar dados públicos da ANS (Agência Nacional de Saúde Suplementar)**, conforme especificado no teste técnico para estágio da **Intuitive Care**.

O desenvolvimento priorizou **clareza**, **organização**, **robustez** e **justificativa técnica**, com foco em qualidade e boas práticas de engenharia de dados.

---

## Objetivos do Projeto

* 🔗 Integração resiliente com a **API de Dados Abertos da ANS**;
* 📆 Identificação automática dos **três últimos trimestres disponíveis**;
* 📦 Processamento de arquivos **heterogêneos** (ZIP, CSV, TXT, XLSX);
* 💸 Consolidação de despesas relacionadas a **Eventos/Sinistros**;
* ✅ Validação, enriquecimento e agregação dos dados;
* 🧠 Documentação e justificativa das **decisões técnicas** e **trade-offs** adotados.

---

## Tecnologias Utilizadas

* **Python 3**
* **pandas**
* **requests**
* **BeautifulSoup**
* **zipfile**
* **venv**

---

## Estrutura do Projeto

O projeto foi organizado seguindo princípios de **separação de responsabilidades**, **baixo acoplamento** e **clareza de fluxo**, adotando uma arquitetura orientada a **pipelines**.

```text
src/
 ├── app/
 │   ├── main.py
 │   └── pipelines/
 │      ├── etapa1_pipeline.py
 │      └── etapa2_pipeline.py
 │   ├── services/
 │   ├── domain/
 │   ├── client/
 │   ├── utils/
 │   └── config/
data/
 ├── temp/      # dados intermediários (descartáveis)
 └── output/    # artefatos finais
```

---

## Como Executar o Projeto

### Requisitos

* Python **3.10+**
* `pip`
* Ambiente virtual (**venv**)

---

### Instalação

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### Execução

O projeto executa automaticamente as **duas etapas do teste** em sequência a partir do arquivo principal:

```bash
python3 src/app/main.py
```

---

## Resultados Gerados

Após a execução, os seguintes artefatos são gerados:

### Etapa 1

* 📦 `data/output/consolidado_despesas.zip`

### Etapa 2

* 📦 `data/output/Teste_Rafael.zip`

  * Contém o arquivo:

    * `despesas_agregadas.csv`

---

## 🔹 Etapa 1 – Coleta, Consolidação e Normalização dos Dados

### Descrição

Na **Etapa 1**, o objetivo foi coletar automaticamente os dados financeiros mais recentes disponibilizados pela ANS, consolidando informações de despesas relacionadas a **Eventos/Sinistros** em um único artefato estruturado.

O pipeline foi projetado para ser **resiliente a mudanças de período**, evitando qualquer dependência de datas fixas ou arquivos previamente conhecidos.

### Estratégia Adotada

* A página de dados abertos da ANS é consumida dinamicamente;
* Os **três últimos trimestres disponíveis** são identificados automaticamente;
* Os arquivos são baixados e extraídos independentemente do formato original;
* Apenas registros relevantes para **Eventos/Sinistros** são mantidos;
* Os dados são consolidados em um único arquivo padronizado.

### Trade-offs e Decisões

**Automação vs. Simplicidade**
Optou-se por identificar os trimestres dinamicamente, aumentando a robustez da solução, mesmo com um custo maior de complexidade inicial.

**Normalização antecipada**
A padronização dos dados ocorre ainda na Etapa 1, reduzindo ruído e facilitando validações e agregações posteriores.

**Armazenamento intermediário**
Dados temporários são persistidos em `data/temp/` para facilitar depuração e inspeção manual durante o desenvolvimento.

---

## 🔹 Validação, Limpeza e Enriquecimento dos Dados

Durante o processamento, foram identificadas **inconsistências naturais em dados públicos**, que exigiram validações explícitas.

### Validações Aplicadas

* CNPJs duplicados associados a diferentes razões sociais;
* Valores zerados ou negativos, incompatíveis com o contexto de despesas;
* Formatos inconsistentes de trimestre e ano;
* Registros incompletos ou com campos críticos ausentes.

### Estratégia de Tratamento

* Nenhum dado foi removido silenciosamente;
* Inconsistências são identificadas, registradas e tratadas conscientemente;
* Em casos ambíguos, optou-se por preservar o dado original, garantindo rastreabilidade;
* O enriquecimento foi realizado apenas quando havia base segura para isso.

Essa abordagem prioriza **transparência**, **auditabilidade** e **confiança** nos resultados finais.

---

## 🔹 Decisões Técnicas e Arquiteturais

### Arquitetura em Pipeline

A solução foi estruturada como uma **pipeline de dados**, permitindo:

* Execução sequencial clara;
* Isolamento de responsabilidades;
* Facilidade de manutenção e extensão;
* Possibilidade de reprocessamento parcial.

### Uso do pandas

O **pandas** foi escolhido por:

* Alta expressividade para manipulação tabular;
* Boa performance para volumes moderados de dados;
* Legibilidade e facilidade de revisão do código.

### Formato de Saída

O formato **CSV** foi adotado por ser:

* Simples;
* Amplamente compatível;
* Fácil de validar e versionar.

Os resultados finais são compactados em **ZIP**, conforme solicitado no teste.

---

## 🔹 Limitações Conhecidas

* O processamento é **single-threaded**;
* Não há persistência em banco de dados;
* Logs são simples e voltados ao desenvolvimento.

Essas escolhas foram conscientes, considerando o **escopo do desafio** e o **tempo de implementação**.

---

## 🔹 Etapa 2 – Análise, Agregação e Ranking das Despesas

### Descrição

Na **Etapa 2**, o objetivo foi analisar os dados consolidados da Etapa 1, realizando o cruzamento com os **dados cadastrais das operadoras** e produzindo agregações finais de despesas, conforme solicitado no teste técnico.

O foco desta etapa está na **integração entre bases distintas**, **padronização semântica** e **geração de um ranking claro e reproduzível**.

---

### Fontes de Dados Utilizadas

Nesta etapa, são combinadas duas fontes principais:

* 📊 **Dados financeiros consolidados** (resultado da Etapa 1);
* 🏢 **Dados cadastrais das operadoras** disponibilizados pela ANS.

Essas bases possuem estruturas, granularidades e objetivos distintos, exigindo tratamento cuidadoso durante o cruzamento.

---

### Estratégia de Processamento

O pipeline da Etapa 2 segue as seguintes etapas:

* Leitura do arquivo consolidado de despesas;
* Leitura e normalização da base cadastral das operadoras;
* Cruzamento das bases utilizando o **CNPJ** como chave principal;
* Validação de correspondência entre registros financeiros e cadastrais;
* Agregação das despesas por operadora;
* Geração do ranking final conforme critério definido no teste.

---

### Chave de Integração e Normalização

* O **CNPJ** foi adotado como chave primária de integração entre as bases;
* Foram aplicadas normalizações para:

  * Remoção de caracteres especiais;
  * Padronização de tipos e formatos;
* Casos de CNPJ sem correspondência cadastral foram **preservados e sinalizados**, evitando descartes indevidos.

Essa decisão garante **rastreabilidade** e evita a perda de informações relevantes.

---

### Agregação e Cálculo dos Resultados

As despesas são agregadas considerando:

* Operadora (CNPJ);
* Razão Social;
* Período de referência (**Trimestre/Ano**);
* Valor total de despesas relacionadas a **Eventos/Sinistros**.

O resultado final é um dataset agregado, pronto para **análise**, **auditoria** ou **visualização**.

---

### Trade-offs e Decisões Técnicas

**Cruzamento explícito vs. enriquecimento automático**
Optou-se por um cruzamento explícito entre as bases, priorizando controle e clareza sobre possíveis inconsistências.

**Preservação de dados incompletos**
Registros sem correspondência cadastral não são descartados automaticamente, evitando viés nos resultados finais.

**Agregação em memória**
A agregação é realizada em memória com **pandas**, suficiente para o volume do desafio e mais simples de manter.

---

### Resultado Final da Etapa 2

O pipeline gera o arquivo final:

* 📄 `despesas_agregadas.csv`

Contendo:

* CNPJ da operadora;
* Razão social;
* Período (**Trimestre/Ano**);
* Valor total agregado de despesas.

Esse arquivo é compactado e entregue conforme especificação do teste em:

* 📦 `data/output/Teste_Rafael.zip`

---

## 🔹 Considerações Finais da Etapa 2

A Etapa 2 consolida o objetivo analítico do desafio, transformando dados brutos e heterogêneos em **informação estruturada e acionável**.

As decisões tomadas priorizaram:

* Clareza dos resultados;
* Transparência no cruzamento de dados;
* Robustez frente a inconsistências reais de bases públicas.

O pipeline foi construído de forma que possa ser facilmente estendido para **novos períodos**, **novas métricas** ou **outras formas de agregação**.