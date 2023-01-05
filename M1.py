import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()


@routes.post("/")
async def filter_data(request):
    try:
        json_data = await request.json()
        print(json_data)
        dictionary = {}
        data = json_data["data"]
        print(data)
        dictionary["username"] = data["username"]
        result = {"data": dictionary}
        async with aiohttp.ClientSession() as session:
            message = await asyncio.create_task(session.get("http://0.0.0.0:8081/JsonData", json=result))
            message = await message.json()
        return web.json_response({"messages": message}, status=200)
    except Exception as e:
        return web.json_response({"serviceNumber": 2, "messages": str(e)}, status=200)


app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8082)
