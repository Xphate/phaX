from Tkinter import *

def controlbutton(labelframe):
    Button(labelframe,
           text="SEND").grid(rowspan=2,column=0)
    Button(labelframe,
           text="RECIEVED").grid(row=0,column=0)