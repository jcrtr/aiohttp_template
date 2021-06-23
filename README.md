# aiohttp_template

AioHTTP project with ultra fast UVloop event loop.

## Requirements

* [aiohttp](https://docs.aiohttp.org/en/stable/)
* [cchardet](https://pypi.org/project/cchardet/)
* [aiodns](https://github.com/saghul/aiodns)
* [aiohttp-cors](https://github.com/aio-libs/aiohttp-cors)
* [aiohttp-session](https://github.com/aio-libs/aiohttp-session)
    * [aioredis](https://github.com/aio-libs/aioredis-py)
* [aiohttp-sqlalchemy](https://github.com/ri-gilfanov/aiohttp-sqlalchemy)
    * [asyncpg](https://github.com/MagicStack/asyncpg)
* [aiohttp_cache](https://github.com/cr0hn/aiohttp-cache)
* [uvloop](https://github.com/MagicStack/uvloop)
* [python-dotenv](https://github.com/theskumar/python-dotenv)


## Installation
### 1. Create venv
### 2. Clone repository
```
git clone https://github.com/likiblack/aiohttp_template.git
```
### 2. Install packages
```
pip install -r requirements.txt
```
### 3. Add settings to .env
```
Default settings

# async sleep

WAIT_TIME = 2

# postgresql

DRIVER = "postgresql+asyncpg" 
USERNAME = ""
PASSWORD = ""
HOST = "127.0.0.1"
PORT = 5432
DATABASE = ""

# cookies

COOKIE_NAME = ""

# session db

REDIS_HOST = "redis://127.0.0.1"
REDIS_DB=''
REDIS_POOL_SIZE = 60
REDIS_TIMEOUT = 60

# cache db (option)

CACHE_HOST = "redis://127.0.0.1"
CACHE_PORT = 6379
CACHE_DB= 0
```
### 4. Run server
```
python main.py
```

### Read the package documentation for solving problems
