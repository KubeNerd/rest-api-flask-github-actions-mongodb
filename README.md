# Objetivo do Projeto

1. **Construir uma REST API com três rotas (endpoints)**:
   - `/users` para retornar todos os usuários (GET)
   - `/user/<cpf>` para retornar um usuário específico (GET)
   - `/user` para registrar um novo usuário (POST)

2. **Persistir dados em um Banco de Dados.**

3. **Configurar a aplicação para rodar dentro de um Docker container (Dockerfile).**

4. **Criar um `docker-compose` para compor a API juntamente com o banco de dados (ambiente de desenvolvimento).**

5. **Escrever testes unitários para as rotas.**

6. **Utilizar um `Makefile` para automatizar os passos mais comuns.**

7. **Fazer o deploy da aplicação em uma plataforma de PaaS (Heroku).**

8. **Criar uma pipeline de CI/CD utilizando alguma ferramenta “as a service” (GitHub Actions, Azure DevOps, etc.).**

A ideia principal é iniciar uma API RESTful usando Flask e, aos poucos, aprimorá-la com boas práticas de desenvolvimento e DevOps. Isso inclui:

- Implementação do padrão de fábrica de aplicação (Application Factory) com Flask-RESTful.
- Utilização do Heroku como plataforma como serviço (PaaS) para deploy contínuo.
- Configuração de um ambiente de homologação usando Docker Compose.
- Utilização de ferramentas de qualidade de código como flake8.
- Implementação de testes automatizados com pytest.
- Uso do GitHub Actions para CI/CD.

Bibliotecas e ferramentas utilizadas:

- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/index.html)
- [Flask-MongoEngine](https://docs.mongoengine.org/projects/flask-mongoengine)
- [Application Factory com Flask](https://flask.palletsprojects.com/en/3.0.x/patterns/appfactories/)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#summary)
- [Configuração do Flask](https://flask.palletsprojects.com/en/1.1.x/config/)
- [Mongomock para testes](https://docs.mongoengine.org/guide/mongomock.html)

## Estrutura

```plaintext
application/
|___ __init__.py
|___ app.py
|___ db.py
|___ model.py
├── tests/
│   └── test_application.py
├── .dockerignore
├── .env
├── .env-sample
├── .gitignore
├── config.py
├── docker-compose.yaml
├── Dockerfile
├── Makefile
├── README.md
├── request.http
├── requirements.txt
└── wsgi.py

```

