from Tkinter import *

def layer2(labelframe,macda,macsa,ethertype,GenerateEther):
    label1 = Message(labelframe, text="MAC    DA",relief=RAISED )   #first input item
    label1.grid(row=0,column=0,sticky=W,ipadx=10)
    text1=Entry(labelframe,textvariable=macda).grid(row=0,column=1)
    label2 = Message(labelframe, text="MAC    SA",relief=RAISED )    #second input item
    label2.grid(row=1,column=0,sticky=W,ipadx=11)
    text2=Entry(labelframe,textvariable=macsa).grid(row=1,column=1)
    label3 = Message(labelframe, text="Ether  Type",relief=RAISED )   #third input item
    label3.grid(row=2,column=0,sticky=W,ipadx=5)
    text3=Entry(labelframe,textvariable=ethertype).grid(row=2,column=1)
    button=Button(labelframe,text="confirm",command=GenerateEther).grid(columnspan=2)    #button of layer2
