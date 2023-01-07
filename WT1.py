from aiohttp import web
import requests

routes = web.RouteTableDef()


@routes.post("/")
async def filter_data(request):
    json_data = await request.json()
    wt1 = []
    for w in json_data:
        if 'username' in w and w['username'].lower().startswith('w'):
            wt1.append(w['username'])

    result1 = wt1
    print(result1)

    url = 'http://127.0.0.1:8085/gatherData'
    requests.post(url, json=result1)

    return web.json_response(result1, status=200)


app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8083)
