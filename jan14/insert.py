import sqlite3

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()

query = """
    INSERT INTO points (x, y)
    VALUES (1, 7);
"""

cursor.execute(query)
conn.commit()
conn.close()