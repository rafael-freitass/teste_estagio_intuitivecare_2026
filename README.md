# 🚀 Teste Técnico – Intuitive Care (Estágio 2026)

## 👨‍💻 Sobre mim

Meu nome é **Rafael Freitas**, sou estudante de **Análise e Desenvolvimento de Sistemas** e atuo profissionalmente na área de TI com desenvolvimento de software e automação.

Tenho interesse especial em:

* Engenharia de dados
* Desenvolvimento backend
* Arquitetura de sistemas
* Automação e integração de APIs
* Construção de aplicações escaláveis e resilientes

Este projeto foi desenvolvido como resposta ao **Teste Técnico de Entrada para Estagiários da Intuitive Care**, com foco em demonstrar:

* Capacidade de resolver problemas reais
* Organização de código
* Pensamento crítico
* Justificativa de decisões técnicas
* Qualidade de documentação

---

# 📌 Visão Geral do Projeto

O objetivo do projeto é construir um pipeline completo que:

1. Consome dados públicos da ANS
2. Processa e normaliza dados heterogêneos
3. Realiza validação e enriquecimento
4. Consolida e agrega informações
5. Armazena e analisa dados em banco relacional
6. Expõe os dados via API REST
7. Disponibiliza visualização via interface web

---

# 🧱 Organização do Projeto

O projeto foi dividido em **módulos independentes**, seguindo separação por responsabilidade e facilitando manutenção, testes e evolução futura.

```
📦 projeto
 ┣ 📂 etapa1_e etapa2
 ┣ 📂 etapa3
 ┣ 📂 etapa4
 ┣ 📄 README.md
```

---

# 📂 Estrutura por Etapa

## 🔹 Etapas 1 e 2 – Pipeline de Dados

📁 `etapa1_e_etapa2/`

Estas duas etapas foram agrupadas propositalmente pois fazem parte do mesmo fluxo lógico de ingestão e tratamento de dados.

### Etapa 1 – Integração com Dados Abertos ANS

Responsável por:

* Descoberta automática de trimestres
* Download resiliente de arquivos
* Extração automática de ZIPs
* Detecção de formatos heterogêneos (CSV, TXT, XLSX)
* Normalização estrutural
* Consolidação de despesas
* Tratamento de inconsistências

### Etapa 2 – Transformação e Enriquecimento

Responsável por:

* Validação de CNPJ
* Validação de valores financeiros
* Join com base cadastral de operadoras
* Tratamento de falhas de relacionamento
* Agregações estatísticas
* Geração de datasets analíticos

---

📄 Cada etapa possui documentação própria:

➡️ Consulte `etapa1_e_etapa2/README.md`

---

## 🔹 Etapa 3 – Banco de Dados e Análise SQL

📁 `etapa3/`

Responsável por:

* Modelagem relacional
* Definição de DDL
* Estratégia de normalização
* Importação massiva de dados
* Indexação e performance
* Desenvolvimento de queries analíticas

---

📄 Documentação detalhada:

➡️ Consulte `etapa3/README.md`

---

## 🔹 Etapa 4 – API e Interface Web

📁 `etapa4/`

Responsável por:

* Exposição dos dados via API REST
* Paginação
* Estatísticas agregadas
* Interface frontend em Vue.js
* Visualização gráfica
* Coleção Postman

---

📄 Documentação detalhada:

➡️ Consulte `etapa4/README.md`,
➡️ Consulte `etapa4/Backend/README.md`, 
➡️ Consulte `etapa4/Frontend/README.md`.


---

## ⚙️ Automação do Pipeline

O pipeline foi estruturado para permitir execução automática completa, reduzindo intervenção manual e simulando cenários de produção.

---

# 🛠️ Tecnologias Utilizadas

## Backend e Dados

* Python
* Pandas
* PostgreSQL
* FastAPI
* SQLAlchemy
* Pydantic

---

## Frontend

* Vue.js
* Chart.js

---

## Ferramentas Auxiliares

* Docker
* Postman
* Git

---

# 📬 Coleção Postman

A coleção contendo todas as rotas da API está disponível em:

```
/etapa4/Teste Tecnico Intuitive Care.postman_collection.json
```

---

# 🧪 Estratégias de Qualidade Aplicadas

Durante o desenvolvimento, busquei:

* Código modular
* Tratamento de exceções
* Logs informativos
* Validação de dados
* Separação clara de responsabilidades
* Documentação detalhada de trade-offs

---

# ⚖️ Trade-offs Técnicos

Cada etapa do projeto apresenta decisões técnicas documentadas em seus respectivos READMEs.

Alguns exemplos:

* Estratégias de validação de CNPJ
* Estratégias de join e enriquecimento
* Normalização vs desnormalização no banco
* Estratégia de paginação da API
* Cache vs cálculo em tempo real
* Estratégias de busca no frontend

---

# 🎯 Principais Desafios Encontrados

* Estrutura inconsistente dos arquivos da ANS
* Alto volume de dados
* Diferenças entre trimestres
* Inconsistências cadastrais
* Balanceamento entre simplicidade e escalabilidade

# 📎 Observações Finais

Este projeto foi desenvolvido priorizando:

✔ Clareza
✔ Manutenibilidade
✔ Resiliência
✔ Justificativa técnica
✔ Simplicidade funcional (KISS)

O objetivo não foi apenas implementar funcionalidades, mas demonstrar raciocínio técnico e capacidade de estruturar soluções reais.
