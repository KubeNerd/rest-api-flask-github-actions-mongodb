# Objetivo do Projeto

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
