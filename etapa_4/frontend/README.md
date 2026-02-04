# 📊 Teste Técnico – Etapa 4: Frontend Vue.js

## 📌 Visão Geral

Esta etapa do teste técnico teve como objetivo o desenvolvimento de uma interface web utilizando **Vue.js 3** para consumo da API desenvolvida nas etapas anteriores.

O frontend foi construído com foco em:

* Organização e clareza na visualização dos dados
* Boa experiência do usuário
* Performance para lidar com grande volume de registros
* Estrutura simples, porém escalável

---

# 🚀 Funcionalidades Implementadas

## ✔ Tabela Paginada de Operadoras

A aplicação apresenta uma tabela contendo as operadoras cadastradas no banco de dados, exibindo:

* CNPJ
* Razão Social
* UF

A tabela possui:

* Paginação controlada pelo backend
* Navegação entre páginas
* Destaque visual indicando que as linhas são clicáveis

Cada operadora pode ser acessada individualmente por meio da navegação para a página de detalhes.

---

## ✔ Busca e Filtro por CNPJ ou Razão Social

Foi implementado um campo de busca que permite filtrar operadoras através dos parâmetros:

* CNPJ
* Razão Social

A busca é enviada diretamente para a API utilizando query parameters:

```
/operadoras?page=1&limit=10&search=texto
```

---

## ✔ Gráfico de Distribuição de Despesas por UF

Foi desenvolvido um gráfico de barras utilizando:

* Chart.js
* Vue-ChartJS

O gráfico apresenta:

* Total de despesas agrupadas por UF
* Visualização clara da concentração geográfica de custos

---

## ✔ Página de Detalhes da Operadora

Ao clicar em uma operadora, o usuário acessa uma página contendo:

* Informações gerais da operadora
* Histórico consolidado de despesas

O histórico é apresentado agrupado por ano, exibindo o total anual de despesas.

Essa abordagem reduz volume de dados exibidos e melhora a legibilidade das informações.

---

# 🧠 Decisões Técnicas e Trade-offs

---

## 4.3.1 Estratégia de Busca e Filtro

### ✔ Escolha: Opção A – Busca no Servidor

A busca foi implementada diretamente na API.

### Motivos da Escolha

O volume de dados disponível contém milhões de registros de despesas e mais de mil operadoras. Manter todos esses dados no cliente causaria:

* Alto consumo de memória
* Lentidão no carregamento inicial
* Possível travamento do navegador

A busca no servidor permite:

* Melhor performance
* Redução do tráfego de dados
* Escalabilidade para bases maiores

### Trade-off

Requer maior número de requisições HTTP. Entretanto, o impacto é mínimo comparado ao ganho de performance e escalabilidade.

---

## 4.3.2 Gerenciamento de Estado

### ✔ Escolha: Opção C – Composables (Vue 3)

Foi utilizado o padrão **Composable** para encapsular a lógica de requisições e estado da aplicação.

### Motivos da Escolha

A aplicação possui complexidade moderada e não exige compartilhamento global intenso de estado.

Os composables oferecem:

* Reutilização de lógica
* Código mais limpo
* Menor complexidade estrutural

### Trade-off

Não possui as ferramentas avançadas de depuração disponíveis em gerenciadores globais como Pinia ou Vuex. Entretanto, para o escopo do projeto, composables são mais leves e suficientes.

---

## 4.3.3 Performance da Tabela

### ✔ Estratégia Utilizada: Paginação no Backend

A tabela carrega apenas uma quantidade limitada de registros por requisição.

### Motivos da Escolha

Carregar todos os registros simultaneamente geraria:

* Alto custo de renderização
* Experiência do usuário degradada
* Alto consumo de memória

A paginação permite:

* Interface responsiva
* Redução de carga no cliente
* Melhor escalabilidade

### Alternativas Consideradas

* Virtual Scroll
* Lazy Loading

Essas alternativas foram descartadas pois aumentariam a complexidade sem trazer ganhos significativos para o escopo atual.

---

## 4.3.4 Tratamento de Erros e Estados da Interface

### ✔ Estados Implementados

#### Loading

Durante requisições à API, mensagens visuais indicam carregamento de dados.

Isso evita que o usuário interprete a ausência de dados como falha do sistema.

---

#### Erros de Rede/API

Mensagens de erro são exibidas quando uma requisição falha.

Foi adotada uma abordagem equilibrada:

* Mensagens compreensíveis para o usuário
* Evita exposição de detalhes técnicos sensíveis

---

#### Dados Vazios

Quando não existem resultados para uma busca ou operadora não possui despesas registradas, mensagens informativas são exibidas.

Isso melhora a experiência do usuário e reduz confusão.

---

# 🧱 Arquitetura do Frontend

A estrutura do projeto foi organizada da seguinte forma:

```
src/
 ├── api/
 ├── assets/
 │    └── styles/
 ├── components/
 ├── composables/
 ├── pages/
 ├── router/
```

### api

Responsável pela comunicação com o backend.

### assets/styles

Contém os arquivos de estilos globais da aplicação.

Essa pasta foi criada com o objetivo de centralizar regras visuais reutilizáveis, evitando repetição de CSS dentro dos componentes.

Os estilos globais incluem:

* Padronização de tipografia
* Estilização base de tabelas
* Componentes visuais reutilizáveis (cards, botões, inputs, etc.)
* Normalização visual entre páginas

Essa abordagem traz benefícios como:

* Melhor manutenção do código
* Maior consistência visual
* Facilidade de expansão futura do design
* Redução de duplicação de estilos em componentes Vue

Os estilos são importados globalmente na aplicação, garantindo que todos os componentes compartilhem a mesma identidade visual.

---

### components

Componentes reutilizáveis como tabelas e gráficos.

### composables

Encapsulam lógica de estado e requisições.

### pages

Representam as telas principais da aplicação.

### router

Gerencia navegação entre páginas.

---

# 🎨 Decisões de UX e Interface

Foram aplicadas estilos visuais simples, porém importantes:

* Destaque visual para elementos clicáveis
* Layout baseado em cartões para organização
* Formatação monetária padronizada
* Botões de navegação intuitivos
* Feedback visual para carregamento
* Padronização global de estilos para consistência visual

---

# ⚙️ Tecnologias Utilizadas

* Vue.js 3
* Vite
* Vue Router
* Chart.js
* Vue-ChartJS
* Fetch API

---

# 🔧 Configuração do Ambiente

## Variáveis de Ambiente

Criar um arquivo `.env` na raiz do projeto frontend:

```
VITE_API_URL=http://127.0.0.1:8000/api/v1
```

---

## Instalação

```
npm install
```

---

## Execução

```
npm run dev
```

---

# ✅ Conclusão

A aplicação frontend atende aos requisitos propostos, oferecendo:

* Visualização clara e organizada dos dados
* Performance adequada para grande volume de registros
* Estrutura modular e escalável
* Experiência de usuário consistente

As decisões técnicas priorizaram simplicidade, escalabilidade e facilidade de manutenção, mantendo alinhamento com boas práticas modernas do ecossistema Vue.js.