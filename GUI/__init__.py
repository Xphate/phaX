from Tkinter import *
import Layer2
import Layer3
import Layer4

top=Tk()                   #top frame
top.title('phaX')
top.geometry('600x700')

macda=StringVar()          #variables for layer2
macsa=StringVar()
ethertype=StringVar()

v = IntVar()                 #variables for layer3
TypeofService=StringVar()
Identification=StringVar()
Flag=StringVar()
Flagoff=StringVar()
TTL=IntVar()
SourceIp=StringVar()
DestinationIp=StringVar()

Protocol=IntVar()            #variables for layer 4
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
Layer3.layer3(labelframe2,v,TypeofService,Identification,Flag,Flagoff,TTL,SourceIp,DestinationIp)



labelframe3=LabelFrame(top,text="layer 4 header")       #frame of layer4
labelframe3.place(x=0,y=405)
Layer4.layer4(labelframe3,Protocol,TypeCode,SourceIp,DestPort,L4Flag,SeqNum,AckNum)




top.mainloop()