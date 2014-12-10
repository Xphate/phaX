from Tkinter import *

def layer3(labelframe,v,TypeofService,Identification,Flag,Flagoff,TTL,SourceIp,DestinationIp,GeneratePkt):
    Radiobutton(labelframe,
            text="arp",
            padx = 20,
            variable=v,
            value=1).grid(row=0,column=0,sticky=W+E+N+S)
    Radiobutton(labelframe,
            text="ipv4",
            padx = 20,
            variable=v,
            value=2).grid(row=0,column=1,sticky=W+E+N+S,padx=0)
    Message(labelframe,
        text="ToS",
        relief=RAISED).grid(row=1,column=0,sticky=W,ipadx=29)
    Entry(labelframe,
      textvariable=TypeofService).grid(row=1,column=1,sticky=E)
    Message(labelframe,
        text="Itag",
        anchor=CENTER,
        relief=RAISED).grid(row=2,column=0,sticky=W,ipadx=28)
    Entry(labelframe,
      textvariable=Identification).grid(row=2,column=1,sticky=E)
    Message(labelframe,
        text="flag",
        relief=RAISED ).grid(row=3,column=0,sticky=W,ipadx=29)
    Entry(labelframe,
      textvariable=Flag).grid(row=3,column=1,sticky=E)
    Message(labelframe,
        text="off",
        relief=RAISED ).grid(row=4,column=0,sticky=W,ipadx=33)
    Entry(labelframe,
      textvariable=Flagoff).grid(row=4,column=1,sticky=E)
    Message(labelframe,
        text="TTL",
        relief=RAISED ).grid(row=5,column=0,sticky=W,ipadx=30)
    Entry(labelframe,
      textvariable=TTL).grid(row=5,column=1,sticky=E)
    Label(labelframe, text="source ip").grid(row=6,column=0,sticky=W)
    Entry(labelframe,
      textvariable=SourceIp).grid(row=7,columnspan=2,ipadx=46)
    Label(labelframe,text="destination ip").grid(row=8,column=0,sticky=W)
    Entry(labelframe,
      textvariable=DestinationIp).grid(row=9,columnspan=2,ipadx=46)
    button=Button(labelframe,text="confirm",command=GeneratePkt).grid(columnspan=2)
