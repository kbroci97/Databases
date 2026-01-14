import sqlite3

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()

query = """
    DELETE FROM points WHERE id = 4;
"""

cursor.execute(query)
conn.commit()
conn.close()