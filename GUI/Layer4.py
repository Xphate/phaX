from Tkinter import *

def layer4(labelframe,Protocol,TypeCode,SourcePort,DestPort,L4Flag,SeqNum,GenerateSegment):
    Radiobutton(labelframe,
            text="TCP",
            padx = 17,
            variable=Protocol,
            value=1).grid(row=0,column=0,sticky=W+E+N+S)
    Radiobutton(labelframe,
            text="UDP",
            padx = 17,
            variable=Protocol,
            value=2).grid(row=0,column=1,sticky=W+E+N+S,padx=0)
    Radiobutton(labelframe,
            text="ICMP",
            padx = 17,
            variable=Protocol,
            value=3).grid(row=0,column=2,sticky=W+E+N+S,padx=0)
    Message(labelframe,
        text="type code",
        relief=RAISED).grid(row=1)
    Entry(labelframe,
      textvariable=TypeCode).grid(row=1,column=1,columnspan=2,sticky=W)
    Message(labelframe,
        text="Source Port",
        relief=RAISED,
        justify=CENTER).grid(row=2,ipadx=9)
    Entry(labelframe,
      textvariable=SourcePort).grid(row=2,column=1,columnspan=2,sticky=W)
    Message(labelframe,
        text="Destina Port",
        relief=RAISED,
        justify=CENTER).grid(row=3,ipadx=8)
    Entry(labelframe,
      textvariable=DestPort).grid(row=3,column=1,columnspan=2,sticky=W)
    Message(labelframe,
        text="Flag",
        relief=RAISED).grid(row=4,ipadx=17)
    Entry(labelframe,
      textvariable=L4Flag).grid(row=4,column=1,columnspan=2,sticky=W)
    Message(labelframe,
        text="Seq Num",
        relief=RAISED,
        justify=CENTER).grid(row=5,ipadx=16)
    Entry(labelframe,
      textvariable=SeqNum).grid(row=5,column=1,columnspan=2,sticky=W)
    button=Button(labelframe,text="confirm",command=GenerateSegment,fg='red').grid(columnspan=3)
