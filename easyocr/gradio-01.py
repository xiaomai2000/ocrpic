import os
from matplotlib import pyplot as plt
import numpy as np
import gradio as gr

### Run it by:  gradio gradio-01.py  ###


# def greet(name):
#     return "Hello " + name + "!"

def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)


# demo = gr.Interface(
#     fn=greet, 
#     inputs=gr.Textbox(lines=2, placeholder="Name here please."), 
#     outputs="text")

demo = gr.Interface(
    fn=greet,
    inputs=["text", gr.Slider(0, 100), "checkbox"],
    outputs=["text", "number"],
)

demo.launch(share=False) 




if __name__ == "__main__":
    print("starts")




