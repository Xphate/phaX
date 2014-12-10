"""
from Tkinter import *
import Layer2
import Layer3
import Layer4
import PacketView
import PacketList
import RecievedPacketList
import RecievedPacketView
import ControlButton


top=Tk()                   #top frame
top.title('phaX')
top.geometry('1500x700')

macda=StringVar()          #variables for layer2
macsa=StringVar()
ethertype=StringVar()

protocol = IntVar()                 #variables for layer3
TypeofService=StringVar()
Identification=StringVar()
Flag=StringVar()
Flagoff=StringVar()
TTL=IntVar()
SourceIp=StringVar()
DestinationIp=StringVar()

Protocol1=IntVar()            #variables for layer 4
TypeCode=StringVar()
SourcePort=IntVar()
DestPort=IntVar()
L4Flag=StringVar()
SeqNum=StringVar()
AckNum=StringVar()

labelframe1 = LabelFrame(top, text="Layer 2 header")   #frame of layer2
labelframe1.place(x=0,y=0)
Layer2.layer2(labelframe1,macda,macsa,ethertype)



labelframe2=LabelFrame(top,text="Layer 3 header")       #frame of layer3
labelframe2.place(x=0,y=130)
Layer3.layer3(labelframe2,protocol,TypeofService,Identification,Flag,Flagoff,TTL,SourceIp,DestinationIp)



labelframe3=LabelFrame(top,text="layer 4 header")       #frame of layer4
labelframe3.place(x=0,y=405)
Layer4.layer4(labelframe3,Protocol1,TypeCode,SourceIp,DestPort,L4Flag,SeqNum,AckNum)


labelframe4=LabelFrame(top,text="Send Packet View")            #frame of Packet View
labelframe4.place(x=270,y=0)
PacketView.packetview(labelframe4)

labelframe5=LabelFrame(top,text="Send Packet List")           #frame of Packet List
labelframe5.place(x=272,y=400)
PacketList.packetlist(labelframe5)

labelframe6=LabelFrame(top,text="Recieved Packet View")       #frame of Recieved Packet View
labelframe6.place(x=725,y=0)
RecievedPacketView.recievedpacketview(labelframe6)

labelframe7=LabelFrame(top,text="Recieved Packet List")        #frame of Recieved Packet List
labelframe7.place(x=725,y=400)
RecievedPacketList.recievedpacketlist(labelframe7)

#labelframe8=LabelFrame(top,text="Control Button")
#labelframe8.place(x=1150,y=0)
#ControlButton.controlbutton(labelframe8)

Button(top,
       text="SEND").place(x=1180,y=250)

Button(top,
       text="RECIEVED").place(x=1180,y=450)

top.mainloop()
"""