from Tkinter import *

def packetlist(labelframe,
               deletepacketlist,
               previouspacketlist,
               nextpacketlist,
               viewpacketlist):
    textlist=[]
    Label(labelframe,
      text="NO.",
      relief=RAISED,
      anchor=W).grid(row=0,column=1,ipadx=3,sticky=W)
    Label(labelframe,
          text="MAC SA",
          relief=RAISED,
          anchor=W).grid(row=0,column=2,ipadx=26,sticky=W)
    Label(labelframe,
          text="MAC DA",
          relief=RAISED,
          anchor=W).grid(row=0,column=3,ipadx=26,sticky=W)
    Label(labelframe,
          text="Packet Name",
          relief=RAISED,
          anchor=W).grid(row=0,column=4,ipadx=20,sticky=W)
    for i in range(10):
        text1=Text(labelframe,
             height=1,
             width=4)
        text1.grid(row=i+1,column=1,sticky=W)
        textlist.append(text1)
        text2=Text(labelframe,
             height=1,
             width=11)
        text2.grid(row=i+1,column=2,sticky=W,ipadx=10)
        textlist.append(text2)
        text3=Text(labelframe,
             height=1,
             width=11)
        text3.grid(row=i+1,column=3,sticky=W,ipadx=10)
        textlist.append(text3)
        text4=Text(labelframe,
             height=1,
             width=17)
        text4.grid(row=i+1,column=4,sticky=W)
        textlist.append(text4)
    Button(labelframe,
           text="Delete",
           command=deletepacketlist).grid(row=2,column=5,sticky=NW,ipadx=6)
    Button(labelframe,
           text="Previous",
           command=previouspacketlist).grid(row=4,column=5,sticky=NW)
    Button(labelframe,
           text="Next",
           command=nextpacketlist).grid(row=6,column=5,sticky=NW,ipadx=10)
    Button(labelframe,
           text="View",
           command=viewpacketlist).grid(row=8,column=5,sticky=NW,ipadx=10)
    return textlist
