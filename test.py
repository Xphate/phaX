from GUI import Layer2,PacketView
from Packet import BuildPacket
from Tkinter import *

top=Tk()                   #top frame
top.title('phaX')
top.geometry('1500x700')

def GenerateEther():
    p=BuildPacket.etherframe(macda.get(),macsa.get(),ethertype.get())
    p.buildetherframe()
    text.insert(END,p.frame.dst)


macda=StringVar()
macsa=StringVar()
ethertype=IntVar()

labelframe1 = LabelFrame(top, text="Layer 2 header")
labelframe1.place(x=0,y=0)
Layer2.layer2(labelframe1,macda,
              macsa,
              ethertype,
              GenerateEther)

labelframe4=LabelFrame(top,text="Send Packet View")            #frame of Packet View
labelframe4.place(x=270,y=0)
text=PacketView.packetview(labelframe4)



top.mainloop()