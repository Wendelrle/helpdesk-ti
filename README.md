# HelpDesk TI

## Sobre o projeto

O HelpDesk TI é um sistema desenvolvido para facilitar o registro, acompanhamento e gerenciamento de chamados de suporte técnico.

O projeto foi desenvolvido como atividade acadêmica do curso de Análise e Desenvolvimento de Sistemas, aplicando conceitos de desenvolvimento em três camadas: front-end, back-end e banco de dados.

## Funcionalidades

### Usuário

- Cadastro de usuários
- Login no sistema
- Abertura de chamados
- Definição de categoria e prioridade
- Visualização dos chamados

### Técnico

- Login e identificação do perfil de técnico
- Painel exclusivo para o técnico
- Visualização dos chamados cadastrados
- Alteração de status: Aberto, Em atendimento e Resolvido
- Filtro de chamados por status
- Contador de chamados
- Visualização da data e hora de criação
- Atribuição de chamados ao técnico responsável (AC3)
- Visualização do técnico responsável pelo chamado (AC3)
- Consulta ao histórico de alterações de status (AC3)
- Registro da data e hora de cada alteração (AC3)

## Tecnologias utilizadas

**Front-end**
- HTML
- CSS
- JavaScript

**Back-end**
- Python
- FastAPI

**Banco de dados**
- PostgreSQL

## Estrutura do projeto

- `frontend/` — Interface e lógica das páginas
- `backend/` — API, conexão com o banco e regras do sistema
- `.gitignore` — Configuração dos arquivos ignorados pelo Git

## Fluxo do sistema

O usuário realiza o cadastro e login e pode abrir chamados informando título, descrição, categoria e prioridade.

Os chamados são registrados inicialmente com o status **Aberto**.

O técnico acessa seu painel, visualiza os chamados, utiliza filtros e altera os status conforme o andamento dos atendimentos.

Na AC3, foi implementada a possibilidade de assumir chamados, registrando o técnico responsável no banco de dados.

Além disso, cada mudança de status é registrada em um histórico, armazenando o status anterior, o novo status e a data e hora da alteração.

O histórico pode ser consultado diretamente pelo Painel do Técnico.

## Evolução do projeto

### AC1 — Estrutura inicial

Desenvolvimento das funcionalidades básicas:

- Cadastro de usuários
- Login
- Abertura de chamados
- Integração entre front-end, back-end e banco de dados

### AC2 — Gerenciamento de chamados

Implementação de:

- Perfil e painel do técnico
- Alteração de status
- Filtros por status
- Contador de chamados
- Registro da data de criação
- Persistência dos dados no PostgreSQL

### AC3 — Atribuição e histórico

Implementação de duas novas funcionalidades:

**1. Atribuição de chamados aos técnicos**

Permite assumir chamados e registrar o técnico responsável pelo atendimento.

**2. Histórico de alterações dos chamados**

Registra automaticamente as mudanças de status, incluindo o status anterior, o novo e a data e hora da alteração.

O histórico pode ser consultado no Painel do Técnico.

## Objetivo

Aplicar na prática os conhecimentos adquiridos no curso de Análise e Desenvolvimento de Sistemas, desenvolvendo uma aplicação integrada com front-end, back-end e banco de dados.

O projeto evolui de forma incremental, incorporando novas funcionalidades a cada etapa acadêmica.
