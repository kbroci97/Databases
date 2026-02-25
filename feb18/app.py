import sqlite3
import pandas as pd
import gradio as gr 

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()

query = """
    WITH topHitters AS (SELECT batting.playerID, nameFirst, nameLast
    FROM batting INNER JOIN people
    ON batting.playerID = people.playerID
    WHERE teamID = 'PHI'
    GROUP BY batting.playerID
    ORDER BY sum(HR) desc
    LIMIT 10)
    
    SELECT CONCAT(nameFirst,' ', nameLast), playerID
    FROM topHitters
    ORDER BY nameLast
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

def f(playerID):
    conn = sqlite3.connect('../baseball.db') 
    cursor = conn.cursor()
    query = """
        SELECT CAST(yearID as text), HR 
        FROM batting 
        WHERE teamID = 'PHI' AND playerID = ? 
        ORDER BY yearID
    """
    cursor.execute(query, [playerID]) 
    records = cursor.fetchall() 
    conn.close() 
    df = pd.DataFrame(records, columns = ["year", "home runs"])
    return df

with gr.Blocks() as iface:
    nameBox = gr.Dropdown(records,interactive = True)
    plot = gr.LinePlot(x = "year", y = "home runs") 
    nameBox.change(fn = f, inputs = [nameBox],outputs = [plot])

iface.launch() 