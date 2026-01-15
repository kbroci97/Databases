import sqlite3
import gradio as gr
import pandas as pd

def fetchPoints():
    conn = sqlite3.connect('my_database.db')

    cursor = conn.cursor()

    query = """
        SELECT * 
        FROM points;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    conn.close()

    df = pd.DataFrame(results, columns = ['id', 'x', 'y'])

    return df

iface = gr.Interface(
    fn = fetchPoints,
    inputs = [],
    outputs = gr.LinePlot(x = 'x', y = 'y', x_lim = (0, 15),y_lim = (0, 15))
)

iface.launch()