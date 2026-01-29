import sqlite3
import pandas as pd

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()

query = """
    SELECT teamID, sum(HR) as teamsHR
    FROM batting
    WHERE yearID = 2025
    GROUP BY teamID
    ORDER BY teamsHR desc;
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records, columns = ['playerID', 'careerHR'])
print(records_df)