from aiohttp import web
from aiohttp_cache import cache


@cache(
    expires=1 * 24 * 3600,
    unless=False,
)
async def home(request):
    return web.Response(text='ok', status=200)
