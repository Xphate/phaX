from Tkinter import *

def packetlist(labelframe):
    Label(labelframe,
      text="Check",
      relief=RAISED).grid(row=0,column=0)
    for i in range(10):
        Checkbutton(labelframe).grid(row=i+1,column=0)
    Label(labelframe,
      text="NO.",
      relief=RAISED,
      anchor=W).grid(row=0,column=1,ipadx=3,sticky=W)
    Label(labelframe,
          text="MAC SA",
          relief=RAISED,
          anchor=W).grid(row=0,column=2,ipadx=15,sticky=W)
    Label(labelframe,
          text="MAC DA",
          relief=RAISED,
          anchor=W).grid(row=0,column=3,ipadx=15,sticky=W)
    Label(labelframe,
          text="Packet Name",
          relief=RAISED,
          anchor=W).grid(row=0,column=4,ipadx=20,sticky=W)
    for i in range(10):
        Text(labelframe,
             height=1,
             width=4).grid(row=i+1,column=1,sticky=W)
        Text(labelframe,
             height=1,
             width=11).grid(row=i+1,column=2,sticky=W)
        Text(labelframe,
             height=1,
             width=11).grid(row=i+1,column=3,sticky=W)
        Text(labelframe,
             height=1,
             width=17).grid(row=i+1,column=4,sticky=W)
    Button(labelframe,
           text="Delete").grid(row=2,column=5,sticky=NW,ipadx=6)
    Button(labelframe,
           text="Previous").grid(row=5,column=5,sticky=NW)
    Button(labelframe,
           text="Next").grid(row=8,column=5,sticky=NW,ipadx=10)
