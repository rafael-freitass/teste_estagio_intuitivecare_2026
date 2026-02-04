# 📊 API de Operadoras - Dados Abertos ANS

## 🧠 Visão Geral

Este projeto consiste no desenvolvimento de uma **API REST em Python** para disponibilizar dados de operadoras de planos de saúde e suas despesas, utilizando dados obtidos da ANS (Agência Nacional de Saúde Suplementar).

A API foi construída com foco em:

* Organização de código
* Escalabilidade
* Performance
* Facilidade de manutenção
* Integração com Frontend Vue.js

Os dados são consumidos e persistidos previamente em banco PostgreSQL (Etapa 3 do projeto).

---

## 🏗️ Arquitetura do Projeto

O projeto segue uma arquitetura modular baseada em boas práticas para APIs REST utilizando FastAPI.

```
src/
 ├── api/
 │   └── v1/
 │        ├── routes/
 │        │     ├── operadoras.py
 │        │     └── estatisticas.py
 │        └── router.py
 │
 ├── config/
 │   └── config.py
 │
 ├── database/
 │   └── database.py
 │
 ├── models/
 │   └── models.py
 │
 ├── schemas/
 │   └── schemas.py
 │
 └── main.py
```

---

## 🧩 Tecnologias Utilizadas

* **FastAPI** – Framework principal da API
* **SQLAlchemy** – ORM para acesso ao banco de dados
* **Pydantic** – Validação e serialização dos dados
* **PostgreSQL** – Persistência dos dados
* **Docker** – Containerização do banco de dados
* **Uvicorn** – Servidor ASGI

---

## 🐳 Banco de Dados

O banco PostgreSQL é executado via Docker.

---

## ⚙️ Configuração de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```
DB_USER=teste_user
DB_PASSWORD=teste_pass
DB_HOST=localhost
DB_PORT=5432
DB_NAME=teste_db

DATABASE_URL=postgresql+psycopg2://teste_user:teste_pass@localhost:5432/teste_db
```

---

## 📦 Instalação

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Subir banco de dados

```bash
docker-compose up -d
```

---

## ▶️ Executando a API

```bash
uvicorn src.main:app --reload
```

A API ficará disponível em:

👉 [http://localhost:8000](http://localhost:8000)

Documentação automática:

👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

# 🚀 Endpoints Disponíveis

## 📌 Operadoras

### Listar Operadoras

```
GET /api/operadoras
```

### Query Params

| Parâmetro | Tipo   | Descrição                      |
| --------- | ------ | ------------------------------ |
| page      | int    | Página atual                   |
| limit     | int    | Quantidade de registros        |
| search    | string | Busca por razão social ou CNPJ |

### Exemplo de Resposta

```json
{
  "data": [],
  "total": 100,
  "page": 1,
  "limit": 10
}
```

---

### Obter Operadora por CNPJ

```
GET /api/operadoras/{cnpj}
```

Retorna os dados detalhados da operadora.

---

### Histórico de Despesas da Operadora

```
GET /api/operadoras/{cnpj}/despesas
```

Retorna todas as despesas relacionadas à operadora.

---

## 📊 Estatísticas

### Estatísticas Gerais

```
GET /api/estatisticas
```

Retorna:

* Total geral de despesas
* Média das despesas
* Top 5 operadoras com maiores despesas

---

### Despesas por UF

```
GET /api/estatisticas/despesas-por-uf
```

Retorna o total consolidado de despesas agrupado por estado.

---

# ⚖️ Trade-offs Técnicos

## 🧩 Escolha do Framework

### ✅ FastAPI

### Alternativas

* Flask

### Justificativa

FastAPI foi escolhido pois:

* Alta performance baseada em Starlette
* Tipagem forte com Python
* Documentação automática com OpenAPI
* Melhor escalabilidade para APIs modernas

Flask é mais simples, porém exigiria maior esforço manual para validação e documentação.

---

## 📄 Estratégia de Paginação

### ✅ Offset-based Pagination

Utiliza os parâmetros:

```
page
limit
```

### Justificativa

* Implementação simples
* Boa integração com frontend
* Adequado para consultas administrativas

Embora cursor pagination seja mais performático em datasets massivos, offset atende bem o escopo atual.

---

## ⚡ Estratégia para Estatísticas

### ✅ Queries Dinâmicas no Banco

### Alternativas

* Cache (Redis)
* Tabelas materializadas

### Justificativa

Como os dados não sofrem atualização frequente:

* Garante consistência dos dados
* Reduz complexidade da infraestrutura

Caso a API passe a receber alto volume de requisições, pode evoluir para cache ou materialização.

---

## 📦 Estrutura de Resposta da API

### ✅ Dados + Metadados

Padronização de respostas para facilitar consumo pelo frontend.

```json
{
  "data": [],
  "total": 100,
  "page": 1,
  "limit": 10
}
```