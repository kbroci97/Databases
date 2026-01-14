import sqlite3

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()

query = """
    CREATE TABLE IF NOT EXISTS points(
        id INTEGER PRIMARY KEY,
        x  REAL,
        y  REAL
    );
"""

cursor.execute(query)
conn.commit()
conn.close()