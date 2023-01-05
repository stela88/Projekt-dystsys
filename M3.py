from aiohttp import web
import asyncio
import aiofiles

routes = web.RouteTableDef()


@routes.post("/gatherData")
async def create_file(request):
    json_data = await request.json()
    list_of_usernames = []
    for username in json_data:
        list_of_usernames.append(username)
    print(list_of_usernames)

    async with aiofiles.open('myfile.txt', mode='w') as f:
        await f.write(username)

        if len(list_of_usernames) > 1:
            tasks = [asyncio.create_task(create_file('myfile.txt'))]

        for task in asyncio.as_completed(tasks):
                result = await task

    return web.json_response(list_of_usernames, status=200)

app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8084)
