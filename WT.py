from aiohttp import web
import requests

routes = web.RouteTableDef()


@routes.post("/")
async def filter_data(request):
    json_data = await request.json()
    wt = []
    for w in json_data:
        if 'username' in w and w['username'].lower().startswith('w'):
            wt.append(w['username'])
    for d in json_data:
        if 'username' in d and d['username'].lower().startswith('d'):
            wt.append(d['username'])

    result = wt
    print(result)

    url = 'http://127.0.0.1:8084/gatherData'
    requests.post(url, json=result)

    return web.json_response(result, status=200)


app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8083)
