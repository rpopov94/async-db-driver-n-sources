# Async database driver 

## Structure

```
project
│   run.py                          # main file 
│   .flake8                         # linter
│   .gitignore                      # gitignore file    
|   poetry.lock                     # utomatically generated file that locks the dependencies 
|   poetry.toml                     # main configuration file for Poetry.
|   README.md                       # description file
|   Dockerfile                      # docker file for fastapi application
|   docker-compose.yml              # docker-compose file
|
└───app
|   └───database
│   |    │   __init__.py             # batch file
│   |    │   models.py               # models this project
|   | 
|   |    __init__.py                # batch file
|   |   app.py                      # main application file     
|   |   routes.py                   # routes this application
|   |   t_data.py                   # set of test data                          
|
└───tests
    |   __init__.py                 # package file
    │   test_serch.py               # set of tests that check the correctness of commands issued via tcp-ip
```

## Dependies

* Python > 3.9
* poetry 1.5.1
* python = "^3.10"
* fastapi = "^0.95.2"
* sqlalchemy = "^2.0.15"
* asyncpg = "^0.27.0"
* python-dotenv = "^1.0.0"
* flake8 = "^6.0.0"
* pytest = "^7.3.1"
* pytest-mock = "^3.10.0"
* pytest-postgresql = "^5.0.0"

## Quick start

For start open terminal and input command

`$ docker-compose up -d --build`

application run with http://0.0.0.0:8000 address

## Run test 

`$ docker-compose exec web pytest .`

### License

MIT