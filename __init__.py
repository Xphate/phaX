from GUI import Gui
from Packet import BuildPacket,CommandAction
from Tkinter import *

#command action
def GenerateEther():
    frame=BuildPacket.etherframe(macda.get(),macsa.get(),ethertype.get())
    frame.buildetherframe()
    newstring="src: "+frame.frame.src+'\n'+"dst: "+frame.frame.dst+'\n'+"type:0x0"
    text1.insert(END,"####[ Ethernet ]####\n",'color')
    text1.insert(END,newstring)
    return frame

def GeneateipPkt():
    pkt=ippacket(tos.get(),id.get(),flags.get(),fragoffset.get(),ttl.get(),sourceip.get(),destinationip.get(),ether.get())
    pkt.buildippacket()
    return pkt

def GeneratearpPkt():
    return

def GenerateTCP():
    return

def GenerateUDP():
    return






top=Tk()
top.title('phaX')
top.geometry('1500x700')

macda=StringVar()               #variables for layer2
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

text1,text2=Gui.mainframe(top,
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
          GeneateipPkt,
          Protocol1,
          TypeCode,
          SourcePort,
          DestPort,
          L4Flag,
          SeqNum,
          AckNum,
          GenerateTCP
          )

mainloop()
