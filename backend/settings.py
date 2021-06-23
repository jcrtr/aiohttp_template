import os
from os.path import join, dirname
from dotenv import load_dotenv
from sqlalchemy.engine import URL

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# TIME
WAIT_TIME = os.environ.get("WAIT_TIME"),

# PG
DB_DSN = URL(
    drivername=os.environ.get("DRIVER"),
    username=os.environ.get("USERNAME"),
    password=os.environ.get("PASSWORD"),
    host=os.environ.get("HOST"),
    port=os.environ.get("PORT"),
    database=os.environ.get("DATABASE"),
)

# COOKIE NAME SESSION
COOKIE_NAME = os.environ.get("COOKIE_NAME")

# REDIS
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_DB = os.environ.get("REDIS_DB")
REDIS_PASS = os.environ.get("REDIS_PASS")
REDIS_POOL_SIZE = os.environ.get("REDIS_POOL_SIZE")
REDIS_TIMEOUT = os.environ.get("REDIS_TIMEOUT")

# CACHED
CACHE_HOST = os.environ.get("CACHE_HOST")
CACHE_PORT = os.environ.get("CACHE_PORT")
CACHE_DB = os.environ.get("CACHE_DB")