from aiohttp import web
import requests

routes = web.RouteTableDef()


@routes.post("/")
async def filter_data(request):
    json_data = await request.json()
    wt2 = []
    for d in json_data:
        if 'username' in d and d['username'].lower().startswith('d'):
            wt2.append(d['username'])

    result2 = wt2
    print(result2)

    url = 'http://127.0.0.1:8085/gatherData'
    requests.post(url, json=result2)

    return web.json_response(result2, status=200)


app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8084)
