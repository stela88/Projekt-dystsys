import json
import asyncio
import aiofiles
import aiohttp
import aiosqlite
from aiohttp import web
import sqlite3
import requests

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM baza_projekt")
count1 = cursor.fetchone()[0]

if count1 == 0:
    print("The database is empty.")
else:
    print("The database is not empty.")

routes = web.RouteTableDef()


@routes.get("/JsonData")
async def json_data(request):
    async with aiofiles.open('file-000000000040.json', mode='r') as file_data:
        read_data = {await file_data.readline() for _ in range(10000)}
        whole_data = [json.loads(line) for line in read_data]
        database = []
        final_result = []
        async with aiosqlite.connect("database.db") as db:
            for item in whole_data:
                db_item = {}
                db_item["username"] = item["repo_name"].rsplit("/", 1)[0]
                db_item["ghlink"] = "https://github.com/" + item["repo_name"] + ".com"
                path_parts = item["path"].rsplit("/", 1)
                if len(path_parts) > 1:
                    db_item["filename"] = path_parts[1]
                else:
                    db_item["filename"] = item["path"]

                database.append(db_item)
                await db.execute(
                    "INSERT INTO baza_projekt (username, ghlink, filename) VALUES (?,?,?)",
                    (
                        db_item["username"], db_item["ghlink"], db_item["filename"]))
            async with db.execute("SELECT * FROM baza_projekt LIMIT 100") as cur:
                columns = [column[0] for column in cur.description]
                result = await cur.fetchall()
                for row in result:
                    final_result.append(dict(zip(columns, row)))
                data = final_result

                url = 'http://127.0.0.1:8080'
                requests.post(url, json=data)

                await db.commit()
        return web.json_response(data, status=200)


app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8081)
