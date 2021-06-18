from aiohttp import web


async def home(request):
    return web.Response(text='ok', status=200)
