# App for DL Academy theory 

[db schema](https://drawsql.app/dl-academy/diagrams/dl-academy-app)
[using libs](./requirements.txt)

## Installation

Create venv

`python3 -m venv venv_name`

Activate

`source venv_name/bin/activate`

Install requirements

`pip install -r requirements.txt`

Project using env variables:

```bash
DATABASE_URL=...
SECRET_KEY=...
HASH_ALGORITHM=...
ACCESS_TOKEN_EXPIRE_MINUTES=...
```

## Run migrations

`alembic upgrade head`

## Run

`uvicorn src.main:app`

