from Tkinter import *


top=Tk()
top.title('phaX')
top.geometry('450x600')

v=IntVar()
TypeCode=StringVar()

Radiobutton(top,
            text="TCP",
            padx = 5,
            variable=v,
            value=1).grid(row=0,column=0,sticky=W+E+N+S)
Radiobutton(top,
            text="UDP",
            padx = 5,
            variable=v,
            value=2).grid(row=0,column=1,sticky=W+E+N+S,padx=0)
Radiobutton(top,
            text="ICMP",
            padx = 5,
            variable=v,
            value=3).grid(row=0,column=2,sticky=W+E+N+S,padx=0)

Message(top,
        text="type code",
        relief=RAISED).grid(row=1)
Entry(top,
      textvariable=TypeCode).grid(row=1,column=1,columnspan=2,sticky=W)

Message(top,
        text="Source Port",
        relief=RAISED,
        justify=CENTER).grid(row=2,ipadx=9)
Entry(top,
      textvariable=TypeCode).grid(row=2,column=1,columnspan=2,sticky=W)

Message(top,
        text="Destina Port",
        relief=RAISED,
        justify=CENTER).grid(row=3,ipadx=8)
Entry(top,
      textvariable=TypeCode).grid(row=3,column=1,columnspan=2,sticky=W)

Message(top,
        text="Flag",
        relief=RAISED).grid(row=4,ipadx=17)
Entry(top,
      textvariable=TypeCode).grid(row=4,column=1,columnspan=2,sticky=W)

Message(top,
        text="Seq Num",
        relief=RAISED,
        justify=CENTER).grid(row=5,ipadx=16)
Entry(top,
      textvariable=TypeCode).grid(row=5,column=1,columnspan=2,sticky=W)

Message(top,
        text="Ack Num",
        relief=RAISED,
        justify=CENTER).grid(row=6,ipadx=16)
Entry(top,
      textvariable=TypeCode).grid(row=6,column=1,columnspan=2,sticky=W)



top.mainloop()