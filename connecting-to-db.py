import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

cursor = conn.cursor()

cursor.execute("""SELECT name FROM sqlite_master WHERE type = 'table';""")
table_name = cursor.fetchall()

cursor.execute("""SELECT * FROM offices;""")
offices_data = cursor.fetchall()

cursor.execute("""SELECT * FROM offices;""").fetchall()
cursor.description


pd.DataFrame(
    data=cursor.execute("""SELECT * FROM offices;""").fetchall(),
    columns=[x[0] for x in cursor.description]
)

print(table_name)
print(offices_data)

conn.close()
