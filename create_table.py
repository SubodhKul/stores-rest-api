import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text,password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

get_table = "SELECT name FROM sqlite_master WHERE type='table'"
result = cursor.execute(get_table)
print(cursor.fetchall())

connection.commit()


connection.close()