from aiohttp import web
import requests

routes = web.RouteTableDef()


@routes.post("/")
async def filter_data(request):
    json_data = await request.json()
    dictionaries = []
    for dictionary in json_data:
        dictionaries.append(dictionary)
    result = dictionaries
    print("result", result)
    url1 = 'http://127.0.0.1:8083/'
    url2 = 'http://127.0.0.1:8084/'
    requests.post(url1, json=result)
    requests.post(url2, json=result)
    return web.json_response(result, status=200)


app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8080)
