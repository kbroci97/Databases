# import pandas as pd

# myList = [(1, 2),(3, 4)]

# df = pd.DataFrame(myList,columns = ['x', 'y'])

# print(df)

#-----------------------

import gradio as gr 

def f(x): 
    return x**2

iface = gr.Interface(
    fn = f, 
    inputs = gr.Number(),
    outputs = gr.Number()
)

iface.launch()