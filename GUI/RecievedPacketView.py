from Tkinter import *

def recievedpacketview(labelframe):
    text=Text(labelframe,
         height=24,width=57)
    text.grid(row=0,column=0)
    return text
