import aiohttp_sqlalchemy
import aioredis
from aiohttp import web
from aiohttp_session import setup
from aiohttp_session.redis_storage import RedisStorage

from settings import DB_DSN, COOKIE_NAME, REDIS_URL, REDIS_TIMEOUT, REDIS_POOL_SIZE
from db import metadata
from routes import init_routes


async def make_redis_pool():
    return await aioredis.create_redis_pool(
        address=REDIS_URL or 'redis://localhost',
        maxsize=int(REDIS_POOL_SIZE) or 10,
        timeout=int(REDIS_TIMEOUT) or 60,
        encoding='utf-8',
    )


async def init_app():
    app = web.Application()

    redis_pool = await make_redis_pool()
    storage = RedisStorage(redis_pool, cookie_name=COOKIE_NAME)

    setup(app, storage)

    aiohttp_sqlalchemy.setup(app, [
        aiohttp_sqlalchemy.bind(DB_DSN),
    ])
    await aiohttp_sqlalchemy.init_db(app, metadata)

    init_routes(app)

    app.on_cleanup.append(cleanup_handler)
    return app


async def startup_handler(app) -> None:
    pass


async def cleanup_handler(app):
    redis_pool = await make_redis_pool()
    redis_pool.close()
    await redis_pool.wait_closed()
