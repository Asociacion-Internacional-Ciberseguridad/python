import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE usuarios (nombre text, edad integer)''')
cursor.execute('''INSERT INTO usuarios VALUES ('Ana', 30)''')
conn.commit()

cursor.execute('SELECT * FROM usuarios')
print(cursor.fetchall())
conn.close()
