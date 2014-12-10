from Tkinter import *

def packetview(labelframe):
    text=Text(labelframe,
         height=24,width=63)
    text.grid(row=0,column=0)
    return text