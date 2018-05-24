# demo-graphql-sqlalchemy-falcon

## Overview

This is a simple project demonstrating the implementation of a GraphQL server in Python using:

- [SQLAlchemy](https://github.com/zzzeek/sqlalchemy).
- [Falcon](https://github.com/falconry/falcon).
- [Graphene](https://github.com/graphql-python/graphene).
- [Graphene-SQLAlchemy](https://github.com/graphql-python/graphene-sqlalchemy).
- [Gunicorn](https://github.com/benoitc/gunicorn).

The objective is to demonstrate how these different libraries can be integrated.

## Features

The primary feature offered by this demo are:

- [SQLAlchemy](https://github.com/zzzeek/sqlalchemy) ORM against a local SQLite database.
- [Falcon](https://github.com/falconry/falcon) resources to serve both [GraphQL](https://github.com/facebook/graphql) and [GraphiQL](https://github.com/graphql/graphiql).

> The [Falcon](https://github.com/falconry/falcon) resources are slightly modified versions of the ones under [https://github.com/alecrasmussen/falcon-graphql-server](https://github.com/alecrasmussen/falcon-graphql-server) so all credits to [Alec Rasmussen](https://github.com/alecrasmussen).

- Basic [GraphQL](https://github.com/facebook/graphql) schema automatically derived from the [SQLAlchemy](https://github.com/zzzeek/sqlalchemy) ORM via [Graphene](https://github.com/graphql-python/graphene) and [Graphene-SQLAlchemy](https://github.com/graphql-python/graphene-sqlalchemy).
- API setup via [Falcon](https://github.com/falconry/falcon) with the whole thing served via [Gunicorn](https://github.com/benoitc/gunicorn).

## Usage

All instructions and commands below are meant to be run from the root dir of this repo.

### Prerequisites

You are strongly encouraged to use a virtualenv here but I can be assed writing down the instructions for that.

Install all requirements through:

```
pip install -r requirements.txt
```

### Sample Database

The sample SQLite database has been committed in this repo but can easily be rebuilt through:

```
python -m demo.orm
```

at which point it will create a `demo.db` in the root of this repo.

> The sample data are defined under `data.py` while they're ingested with the code under the `main` sentinel in `orm.py`. Feel free to tinker.

### Running Server

The [Gunicorn](https://github.com/benoitc/gunicorn) is configured via the `gunicorn_config.py` module and binds by default to `localhost:5432/`. You can change all gunicorn configuration options under the aforementioned module.

The server can be run through:

```
gunicorn -c gunicorn_config.py "demo.demo:main()"
```

The server exposes two endpoints:

- `/graphql`: The standard GraphQL endpoint which can receive the queries directly (accessible by default under [http://localhost:5432/graphql](http://localhost:5432/graphql)).
- `/graphiql`: The [GraphiQL](https://github.com/graphql/graphiql) interface (accessible by default under [http://localhost:5432/graphiql](http://localhost:5432/graphiql)).
