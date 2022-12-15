import sqlite3


conn = sqlite3.connect('database.db')
cursor = conn.cursor()


cursor.execute("SELECT COUNT(*) FROM baza_projekt")
count1 = cursor.fetchone()[0]


if count1 == 0:
    print("The database is empty.")
else:
    print("The database is not empty.")


query = 'SELECT id,username,ghlink,filename FROM baza_projekt'

results = cursor.execute(query)

for row in results:
    print(row)

conn.close()



