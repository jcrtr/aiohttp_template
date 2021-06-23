from aiohttp import web
from routes import init_routes

import aiohttp_sqlalchemy
import aioredis
from aiohttp_session import setup
from aiohttp_session.redis_storage import RedisStorage

from aiohttp_cache import setup_cache

from settings import \
    DB_DSN, \
    COOKIE_NAME, \
    REDIS_HOST, REDIS_TIMEOUT, REDIS_POOL_SIZE, REDIS_DB, REDIS_PASS \
    # CACHE_DB, CACHE_HOST, CACHE_PORT

from db import metadata


async def make_redis_pool():
    return await aioredis.create_redis_pool(
        address=REDIS_HOST or "redis://127.0.0.1",
        # db=REDIS_DB,
        # password=REDIS_PASS,
        maxsize=int(REDIS_POOL_SIZE) or 10,
        timeout=int(REDIS_TIMEOUT) or 60,
        encoding='utf-8',
    )


async def init_app():
    app = web.Application()
    redis_session = await make_redis_pool()
    storage = RedisStorage(redis_session, cookie_name=COOKIE_NAME)

    # aiohttp_sqlalchemy.setup(app, [
    #     aiohttp_sqlalchemy.bind(DB_DSN),
    # ])
    # await aiohttp_sqlalchemy.init_db(app, metadata)

    init_routes(app)
    setup(app, storage)
    setup_cache(app)
    app.on_cleanup.append(cleanup_handler)
    return app


async def startup_handler(app) -> None:
    pass


async def cleanup_handler(app) -> None:
    redis_session = await make_redis_pool()
    redis_session.close()
    await redis_session.wait_closed()
