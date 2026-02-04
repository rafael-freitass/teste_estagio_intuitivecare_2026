# 🌐 Etapa 4 – API e Interface Web

## 📌 Visão Geral

Esta etapa tem como objetivo disponibilizar os dados processados nas etapas anteriores através de uma API REST em Python e de uma interface web desenvolvida em Vue.js.

A solução foi dividida em dois módulos principais:

* Backend: Responsável pela disponibilização dos dados e regras de negócio através de uma API REST.
* Frontend: Responsável pela visualização dos dados e interação com o usuário.

Os dados utilizados são provenientes do banco criado na Etapa 3.

---

# 🏗️ Arquitetura da Solução

```
Frontend (Vue.js)
        ↓
Backend (FastAPI)
        ↓
Banco de Dados PostgreSQL
```

# 📬 Documentação da API – Postman

Foi criada uma coleção do Postman contendo todos os endpoints da API.

## 📦 Estrutura da Collection

### Operadoras

* Listagem geral
* Consulta por CNPJ
* Consulta de despesas por CNPJ

### Estatísticas

* Estatísticas gerais
* Despesas por UF

---

## ▶️ Como Importar a Collection

1. Abra o Postman
2. Clique em **Import**
3. Selecione o arquivo JSON da collection
4. Configure a variável `baseUrl` apontando para o servidor

Exemplo:

```
http://localhost:8000
```

---

## 📤 Explicação da Exportação da Collection

A collection foi exportada no formato **Postman Collection v2.1**, que é o padrão suportado pela ferramenta.

### 🔹 Estrutura do Arquivo

O JSON exportado contém:

* Informações da collection
* Organização em pastas
* Definição das rotas
* Variáveis dinâmicas

---

### 🔹 Uso de Variáveis

Foram utilizadas variáveis para facilitar testes:

* `{{baseUrl}}` – URL base da API
* `{{cnpj}}` – CNPJ da operadora

Isso permite alterar facilmente o ambiente sem modificar cada requisição.

---

### 🔹 Objetivo da Collection

A collection permite:

* Testar todos os endpoints rapidamente
* Documentar exemplos de requisição
* Facilitar validação da API
* Auxiliar integração com frontend

---

# 📁 Explicações do projeto

```
etapa4/
 ├── backend/
 │   └── README.md
 ├── frontend/
 │   └── README.md
 └── README.md
```