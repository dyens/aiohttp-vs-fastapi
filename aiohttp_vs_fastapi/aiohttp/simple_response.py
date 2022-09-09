from aiohttp import web


async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    return web.json_response({"name": name})


app = web.Application()
app.add_routes([web.get("/{name}", handle)])


def run():
    web.run_app(app)
