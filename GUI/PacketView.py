from Tkinter import *

def packetview(labelframe):
    text1=Text(labelframe,
               height=4,
               width=63)
    text1.grid(row=0,column=0)
    text2=Text(labelframe,
               height=4,
               width=63)
    text2.grid(row=1,column=0)
    text3=Text(labelframe,
               height=4,
               width=63)
    text3.grid(row=2,column=0)
    text4=Text(labelframe,
               height=4,
               width=63)
    text4.grid(row=3,column=0)
    text5=Text(labelframe,
               height=7,
               width=63)
    text5.grid(row=4,column=0)
    return text1,text2,text3,text4,text5