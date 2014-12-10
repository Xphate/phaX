from Tkinter import *
import Layer2
import Layer3
import Layer4
import PacketView
import PacketList
import RecievedPacketList
import RecievedPacketView
import ControlButton

def mainframe(top,
              macda,
              macsa,
              ethertype,
              GenerateEther,
              protocol,
              TypeofService,
              Identification,
              Flag,
              Flagoff,
              TTL,
              SourceIp,
              DestinationIp,
              GeneratePkt,
              Protocol1,
              TypeCode,
              SourcePort,
              DestPort,
              L4Flag,
              SeqNum,
              AckNum,
              GenerateSegment
              ):
    labelframe1 = LabelFrame(top, text="Layer 2 header")   #frame of layer2
    labelframe1.place(x=0,y=0)
    Layer2.layer2(labelframe1,macda,macsa,ethertype,GenerateEther)

    labelframe2=LabelFrame(top,text="Layer 3 header")       #frame of layer3
    labelframe2.place(x=0,y=130)
    Layer3.layer3(labelframe2,protocol,TypeofService,Identification,Flag,Flagoff,TTL,SourceIp,DestinationIp,GeneratePkt)

    labelframe3=LabelFrame(top,text="layer 4 header")       #frame of layer4
    labelframe3.place(x=0,y=405)
    Layer4.layer4(labelframe3,Protocol1,TypeCode,SourceIp,DestPort,L4Flag,SeqNum,AckNum,GenerateSegment)

    labelframe4=LabelFrame(top,text="Send Packet View")            #frame of Packet View
    labelframe4.place(x=270,y=0)
    text1=PacketView.packetview(labelframe4)

    labelframe5=LabelFrame(top,text="Send Packet List")           #frame of Packet List
    labelframe5.place(x=272,y=400)
    PacketList.packetlist(labelframe5)

    labelframe6=LabelFrame(top,text="Recieved Packet View")       #frame of Recieved Packet View
    labelframe6.place(x=725,y=0)
    text2=RecievedPacketView.recievedpacketview(labelframe6)

    labelframe7=LabelFrame(top,text="Recieved Packet List")        #frame of Recieved Packet List
    labelframe7.place(x=725,y=400)
    RecievedPacketList.recievedpacketlist(labelframe7)
    #labelframe8=LabelFrame(top,text="Control Button")
    # #labelframe8.place(x=1150,y=0)
    # #ControlButton.controlbutton(labelframe8)
    Button(top,
           text="SEND").place(x=1180,y=250)
    Button(top,
           text="RECIEVED").place(x=1180,y=450)
    return text1,text2
