# HelpDesk TI

## Sobre o projeto

O HelpDesk TI é um sistema desenvolvido para facilitar o registro, acompanhamento e gerenciamento de chamados de suporte técnico.

O projeto foi desenvolvido como atividade acadêmica do curso de Análise e Desenvolvimento de Sistemas, aplicando conceitos de desenvolvimento em três camadas: front-end, back-end e banco de dados.

## Funcionalidades

### Usuário

- Cadastro de usuários
- Login no sistema
- Abertura de chamados
- Definição de categoria
- Definição de prioridade
- Visualização dos chamados

### Técnico

- Login e identificação do perfil de técnico
- Painel exclusivo para o técnico
- Visualização dos chamados cadastrados
- Alteração do status dos chamados
- Status: Aberto, Em atendimento e Resolvido
- Filtro de chamados por status
- Contador de chamados
- Visualização da data e hora de criação do chamado

## Tecnologias utilizadas

### Front-end

- HTML
- CSS
- JavaScript

### Back-end

- Python
- FastAPI

### Banco de Dados

- PostgreSQL

## Estrutura do projeto

- `frontend/` - Interface e lógica das páginas do sistema
- `backend/` - API, conexão com banco de dados e regras do sistema
- `.gitignore` - Configuração dos arquivos e pastas ignorados pelo Git

## Fluxo do sistema

O usuário realiza o cadastro e login no sistema e pode abrir chamados informando título, descrição, categoria e prioridade.

Os chamados são registrados inicialmente com o status **Aberto**.

O técnico possui acesso a um painel específico, onde pode visualizar os chamados cadastrados, filtrar por status e alterar o andamento para **Aberto**, **Em atendimento** ou **Resolvido**.

## Evolução do projeto

### AC1

Desenvolvimento da estrutura inicial do HelpDesk TI, incluindo cadastro, login, abertura de chamados e integração entre front-end, back-end e banco de dados.

### AC2

Evolução do sistema com a criação do perfil de técnico, painel de gerenciamento, alteração e filtro de status, contador de chamados e registro da data de criação.

## Objetivo

O objetivo do projeto é aplicar na prática conceitos estudados no curso de Análise e Desenvolvimento de Sistemas, desenvolvendo uma aplicação integrada com front-end, back-end e banco de dados.
