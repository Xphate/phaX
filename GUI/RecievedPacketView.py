from Tkinter import *

def recievedpacketview(labelframe):
    text=Text(labelframe,
               height=25,
               width=65)
    text.grid(row=0,column=0)
    return text
