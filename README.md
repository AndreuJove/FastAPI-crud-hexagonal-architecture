# FastAPI Crud Hexagonal Architecture

Python FastAPI API service, backed by SQLite using SQLAlchemy.

## Requirements:

Docker: https://docs.docker.com/engine/install/


## Documentation:

FastAPI mounts openapi documentation in /docs. After running the server you can go to http://0.0.0.0:8000/docs to see it.
Moreover you can find it in: /docs/openapi.json


## Run server:

  ```bash
docker build -f docker/Dockerfile -t flaskapi-crud-image:0.0.1 .
docker run -p 8000:8000 flaskapi-crud-image:0.0.1
  ```


## Run tests:

  ```bash
docker build -f docker/Dockerfile.test -t flaskapi-crud-tests:0.0.1 .
docker run flaskapi-crud-tests:0.0.1
  ```


## Pending (not enough time to do it):

- Do CI with linters(flake8, mypy, etc..) and formatters, and tests.
- Improve set up of docker with scripts.
- Add precommits hooks.
- Do more testing/improve.
- Do CD.
- Define different environment variables envs.
- Docker compose with Volumes for persistent data.
