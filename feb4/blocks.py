import sqlite3
import gradio as gr
import pandas as pd

def fetchPhillies():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
       SELECT playerID
       FROM batting
       WHERE yearID = 1976 AND teamID = 'PHI';
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()

    players = []
    for record in records: 
        players.append(record[0])
    return players

def f(player):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT HR 
        FROM batting
        WHERE yearID = 1976 AND teamID = 'PHI' AND playerID = ?;
    """
    cursor.execute(query, [player])
    records = cursor.fetchall()
    conn.close()
    return records[0][0] 

with gr.Blocks() as iface:  
    iBox = gr.Dropdown(fetchPhillies(), label = "Select a player", value = None)
    oBox = gr.Number(label="This is the sum of those numbers")

    iBox.change(fn = f, inputs = [iBox], outputs = [oBox])

iface.launch() 