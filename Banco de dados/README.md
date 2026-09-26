# Banco de Dados & POO

Repositório com as atividades da disciplina de Banco de Dados e Programação Orientada a Objetos (UNIP).

## Estrutura

```
├── Atv0809/   # Atividade de 09/08 — Explorando o BD PostgreSQL (Docker + pgAdmin)
├── Atv2508/   # Atividade de 25/08
└── Atv3108/   # Atividade de 31/08
```

## Atv0809 — Explorando o BD PostgreSQL

Configuração de um ambiente PostgreSQL + pgAdmin via Docker Compose, seguido da criação e
manipulação de tabelas via SQL:

- Criação do arquivo `docker-compose.yml` com os serviços `postgres` e `pgadmin`
- Conexão do banco PostgreSQL ao pgAdmin
- Criação de tabela (`CREATE TABLE`)
- População da tabela com dados de teste
- Consultas de filtro (`SELECT ... WHERE`)

## Como rodar

1. Instale o [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Dentro da pasta da atividade, rode:
   ```
   docker-compose up
   ```
3. Acesse o pgAdmin em `http://localhost:5050`
4. Use as credenciais definidas no `docker-compose.yml` para conectar ao PostgreSQL

## Tecnologias

- PostgreSQL
- pgAdmin
- Docker / Docker Compose
- SQL
