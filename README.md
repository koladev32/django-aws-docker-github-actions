# django-auth-react-tutorial

## Create a virtual environment

```shell
virtualenv --python=/usr/bin/python3.8 venv
```

## Install requirements

```shell
pip install -r requirements.txt
```

## Env Vars

Make sure to provide the necessary environment variables. 
Create a `.env` file in the root directory and follow the structure of the `.env.example` file.

## Migrate and Start the server

```shell
python manage.py migrate
python manage.py runserver
```

## Docker 

> Start the app in Docker

### Development environment
```bash
$ docker-compose up -f docker-compose.dev.yml --build -d
```

### Production environment

```bash
$ docker-compose up --build -d
```


Visit `http://localhost` in your browser. The API server will be running.

