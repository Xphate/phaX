from Tkinter import *
import Layer2
import Layer3
import Layer4
import PacketView
import PacketList
import RecievedPacketList
import RecievedPacketView
import ControlButton
from tkFileDialog import askopenfilename

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
              GenerateSegment,
              Clear,
              Generate,
              deletepacketlist,
              previouspacketlist,
              nextpacketlist,
              viewpacketlist,
              sendfull,
              callback):
    labelframe1 = LabelFrame(top, text="Layer 2 header")   #frame of layer2
    labelframe1.place(x=0,y=0)
    Layer2.layer2(labelframe1,macda,macsa,ethertype,GenerateEther)

    labelframe2=LabelFrame(top,text="Layer 3 header")       #frame of layer3
    labelframe2.place(x=0,y=130)
    Layer3.layer3(labelframe2,protocol,TypeofService,Identification,Flag,Flagoff,TTL,SourceIp,DestinationIp,GeneratePkt)

    labelframe3=LabelFrame(top,text="layer 4 header")       #frame of layer4
    labelframe3.place(x=0,y=405)
    Layer4.layer4(labelframe3,Protocol1,TypeCode,SourcePort,DestPort,L4Flag,SeqNum,GenerateSegment)

    labelframe4=LabelFrame(top,text="Send Packet View")            #frame of Packet View
    labelframe4.place(x=270,y=0)
    text1,text2,text3,text4,text5=PacketView.packetview(labelframe4)

    labelframe5=LabelFrame(top,text="Send Packet List")           #frame of Packet List
    labelframe5.place(x=272,y=400)
    textlist=PacketList.packetlist(labelframe5,
                                   deletepacketlist,
                                   previouspacketlist,
                                   nextpacketlist,
                                   viewpacketlist)

    labelframe6=LabelFrame(top,text="Detailed Information Of Packet")       #frame of Recieved Packet View
    labelframe6.place(x=725,y=0)
    text6=RecievedPacketView.recievedpacketview(labelframe6)



    labelframe8=LabelFrame(top)
    labelframe8.place(x=0,y=640)
    Button(labelframe8,
           text="Clear",
           command=Clear,
           fg='red').grid(row=0,column=0,ipadx=30)
    Button(labelframe8,
           text="Generate",
           command=Generate,
           fg='red').grid(row=0,column=1,ipadx=30)

    labelframe9=LabelFrame(top)
    labelframe9.place(x=850,y=520)

    Button(labelframe9,
           text="SEND",
           command=sendfull,
           fg='red').grid(row=0,column=0,ipadx=35,ipady=20)
    Button(labelframe9,
           text='File Open',
           command=callback,
           fg='red').grid(row=0,column=1,ipadx=20,ipady=20)
    return text1,text2,text3,text4,text5,text6,textlist
