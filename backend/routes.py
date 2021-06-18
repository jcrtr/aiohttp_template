import aiohttp_cors

from views import home


def init_routes(app):
    r = app.router

    r.add_route("GET", '/', home)

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    for route in list(r.routes()):
        cors.add(route)
