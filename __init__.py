from GUI import Gui
from Packet import PacketCode,GeneratePacket
from Tkinter import *
from lib import InputCheck
from tkMessageBox import *
from FileDialog import *
from scapy.all import *
import sys
from lib import Stack

frame=Ether()
ippkt=IP()
arppkt=ARP()
tcpseg=TCP()
udpseg=UDP()
icmpseg=ICMP()
full=Ether()/IP()/TCP()
from tkFileDialog import askopenfilename

mystack=Stack.stack()

hand=1

#command action
def GenerateEther():
    global frame
    state=(InputCheck.MacCheck(macda.get()))and(InputCheck.MacCheck(macsa.get()))
    if state==0:
        showerror(title="ERROR",message="you have inputed wrong mac format")
    else:
        frame=Ether(src=macda.get(),dst=macsa.get(),type=ethertype.get())
        text1.delete('1.0',END)
        newstring="src: "+frame.src+'\n'+"dst: "+frame.dst+'\n'+"type: "+str(frame.type)+'\n'
        text1.tag_config('a',foreground = 'red')
        text1.insert(END,"####[ Ethernet ]####\n",'a')
        text1.tag_config('b',foreground='blue')
        text1.insert(END,newstring,'b')

def GeneratePkt():
    global arppkt
    global ippkt
    if protocol.get()==1:
        state=state=(InputCheck.IpCheck(SourceIp.get()))and(InputCheck.IpCheck(DestinationIp.get()))
        if state==0:
            showerror(title="ERROR",message="you have inputed wrong ip format")
        else:
            arppkt=ARP(psrc=SourceIp.get(),
                       pdst=DestinationIp.get(),
                       hwsrc=frame.src)
            text2.delete('1.0',END)
            text2.tag_config('a',foreground='red')
            text2.insert(END,'####[ ARP ]####\n','a')
            text2.tag_config('b',foreground='blue')
            newstring1='hwtype: '+str(arppkt.hwtype)+'   '+'ptype: '+str(arppkt.ptype)+'   '+'hwlen: '+str(arppkt.hwlen)+'   '+'plen: '+str(arppkt.plen)+'\n'
            newstring2='op:     '+str(arppkt.op)+'   '+"hwsrc: "+arppkt.hwsrc+'   '+'hwdst: '+arppkt.hwdst+'\n'
            newstring3='psrc:   '+arppkt.psrc+'   '+'pdst: '+arppkt.pdst
            text2.insert(END,newstring1,'b')
            text2.insert(END,newstring2,'b')
            text2.insert(END,newstring3,'b')
    elif protocol.get()==2:
        state=(InputCheck.IpCheck(SourceIp.get()))and(InputCheck.IpCheck(DestinationIp.get()))and(InputCheck.TTLCheck(TTL.get()))
        if state==1:
            ippkt=IP(ttl=TTL.get(),
                     tos=TypeofService.get(),
                     id=Identification.get(),
                     flags=Flag.get(),
                     frag=Flagoff.get(),
                     src=SourceIp.get(),
                     dst=DestinationIp.get())
            text2.delete('1.0',END)
            text2.tag_config('a',foreground='red')
            text2.insert(END,"####[ IP ]####\n",'a')
            newstring1="version: "+str(ippkt.version)+"    "+"ihl: "+str(ippkt.ihl)+'    '
            newstring2="tos:     "+str(ippkt.tos)+'    '+"len: "+str(ippkt.len)+'\n'
            newstring3="id       "+str(ippkt.flags)+'    '+"frag: "+str(ippkt.frag)+'      '
            newstring4="ttl: "+str(ippkt.ttl)+'      '+"proto: "+str(ippkt.proto)+'\n'
            newstring5="src: "+ippkt.src+'     '+"dst:"+ippkt.dst
            text2.tag_config('b',foreground='blue')
            text2.insert(END,newstring1,'b')
            text2.insert(END,newstring2,'b')
            text2.insert(END,newstring3,'b')
            text2.insert(END,newstring4,'b')
            text2.insert(END,newstring5,'b')
        else:
            showerror(title="ERROR",message="you have inputed wrong ip format or ttl")
    else:
        showerror(title="ERROR",message="you do not choose any protocol")


def GenerateSeg():
    global tcpseg
    global udpseg
    global icmpseg
    if Protocol1.get()==1:
        state=(InputCheck.PortCheck(SourcePort.get()))and(InputCheck.PortCheck(DestPort.get()))
        if state==1:
            tcpseg=TCP(sport=SourcePort.get(),
                       dport=DestPort.get(),
                       seq=SeqNum.get(),
                       ack=AckNum.get(),
                       flags=L4Flag.get())
            text3.delete('1.0',END)
            text3.tag_config('a',foreground='red')
            text3.tag_config('b',foreground='blue')
            text3.insert(END,'####[ TCP ]####\n','a')
            newstring1="sport: "+str(tcpseg.sport)+'   '+"dport: "+str(tcpseg.dport)+'   '
            newstring2="seg: "+str(tcpseg.seq)+'   '+"ack: "+str(tcpseg.ack)+'\n'
            newstring3="dataofs: "+str(tcpseg.dataofs)+'   '+"reserved: "+str(tcpseg.reserved)+'   '
            newstring4="flag: "+str(tcpseg.flags)+'   '+"window: "+str(tcpseg.window)+'\n'
            newstring5="chksum: "+str(tcpseg.chksum)+'   '+"urgptr: "+str(tcpseg.urgptr)+'   '
            newstring6="options: "+str(tcpseg.options)
            for i in range(1,7):
                astring="newstring"+str(i)
                text3.insert(END,eval(astring),'b')
        else:
            showerror(title="ERROR",message="you have inputed wrong port format")
    elif Protocol1.get()==2:
        state=(InputCheck.PortCheck(SourcePort.get()))and(InputCheck.PortCheck(DestPort.get()))
        if state==1:
            udpseg=UDP(sport=SourcePort.get(),
                       dport=DestPort.get())
            text3.delete('1.0',END)
            text3.tag_config('a',foreground='red')
            text3.tag_config('b',forground='blue')
            text3.insert(END,'####[ UDP }####\n','a')
            newstring1="sport: "+str(udpseg.sport)+'   '+"dport: "+str(udpseg.dport)+'\n'
            newstring2='len:   '+str(udpseg.len)+'    '+'chksum: '+str(udpseg.chksum)+'\n'
            text3.insert(END,newstring1,'b')
            text3.insert(END,newstring2,'b')
        else:
            showerror(title="ERROR",message="you have inputed wrong port format")
    elif  Protocol1.get()==3:
        state=InputCheck.icmptypecheck(TypeCode.get())
        if state==1:
            icmpseg=ICMP(type=TypeCode.get())
            text3.delete('1.0',END)
            text3.delete('1.0',END)
            text3.tag_config('a',foreground='red')
            text3.tag_config('b',foreground='blue')
            text3.insert(END,"####[ ICMP ]####\n",'a')
            newstring1="type: "+PacketCode.icmpcode[icmpseg.type]+'   '+"code: "+str(icmpseg.code)+'\n'
            newstring2="chksum: "+str(icmpseg.chksum)+'   '+"id: "+str(icmpseg.id)+'   '+"seq: "+str(icmpseg.seq)+'\n'
            text3.insert(END,newstring1,'b')
            text3.insert(END,newstring2,'b')
        else:
            showerror(title="EROOR",message="you have inputed wrong type code")
    else:
        showerror(title="ERROR",message="you have not choosen any protocol")

def Clear():
    global frame,ippkt,arppkt,tcpseg,udpseg,icmpseg,full
    text1.delete('1.0',END)
    text2.delete('1.0',END)
    text3.delete('1.0',END)
    text4.delete('1.0',END)
    text5.delete('1.0',END)
    text4.tag_config('a',foreground='gray')
    text4.insert(END,"input somthing....",'a')
    frame=Ether()
    ippkt=IP()
    arppkt=ARP()
    tcpseg=TCP()
    udpseg=UDP()
    icmpseg=ICMP()
    full=Ether()/IP()/TCP()
    return

def Generate():
    global frame,ippkt,arppkt,tcpseg,udpseg,icmpseg,full,s
    text5.delete('1.0',END)
    c=str(text4.get('1.0',END))
    a=protocol.get()
    b=Protocol1.get()
    if c=="input something....\n" or c=="Packets have been sended...\n":
        if a==1:
            full=frame/arppkt
        elif a==2 and b!=1 and b!=2 and b!=3:
            full=frame/ippkt
        elif a==2 and b==1:
            full=frame/ippkt/tcpseg
        elif a==2 and b==2:
            full=frame/ippkt/udpseg
        elif a==2 and b==3:
            full=frame/ippkt/icmpseg
        else:
            full=frame/IP()/TCP()
    else:
        if a==1:
            full=frame/arppkt/c
        elif a==2 and b!=1 and b!=2 and b!=3:
            full=frame/ippkt/c
        elif a==2 and b==1:
            full=frame/ippkt/tcpseg/c
        elif a==2 and b==2:
            full=frame/ippkt/udpseg/c
        elif a==2 and b==3:
            full=frame/ippkt/icmpseg/c
        else:
            full=Ether()/IP()/TCP()/c
    mystack.Push(full)
    f_handler=open('./lib/generate.txt','w')
    sys.stdout=f_handler
    hexdump(full)
    f_handler.close()
    f_handler=open('./lib/generate.txt','r')
    data=[line.strip() for line in f_handler.readlines()]
    i=0
    while i<len(data):
        text5.insert(END,data[i])
        text5.insert(END,'\n')
        i=i+1
    f_handler.close()
    f=open('/lib/log.txt','w')
    sys.stdout=f
    viewpacketlist()
    return


def deletepacketlist():
    global hand
    mystack.Pop()
    viewpacketlist()
    hand=1
    if mystack.IsEmpty():
        text5.delete('1.0',END)
        text6.delete('1.0',END)
    return

def previouspacketlist():
    global hand
    weight=mystack.len/10
    if mystack.len>10:
        tmp=10
    else:
        tmp=mystack.len
    if 1<=hand and hand<=tmp:
        viewpacketlist()
        for i in range(4):
            tmp=textlist[i].get('1.0',END)
            textlist[i].delete('1.0',END)
            textlist[i].insert(END,tmp)
        if hand>1:
            hand=hand-1
        else:
            for i in range(4):
                tmp=textlist[4*(hand-1)+i].get('1.0',END)
                textlist[4*(hand-1)+i].tag_config('a',foreground='red')
                textlist[4*(hand-1)+i].delete('1.0',END)
                textlist[4*(hand-1)+i].insert(END,tmp,'a')
        for i in range(4):
            tmp=textlist[4*(hand-1)+i].get('1.0',END)
            textlist[4*(hand-1)+i].tag_config('a',foreground='red')
            textlist[4*(hand-1)+i].delete('1.0',END)
            textlist[4*(hand-1)+i].insert(END,tmp,'a')
    else:
        for i in range(4):
            tmp=textlist[i].get('1.0',END)
            textlist[i].tag_config('a',foreground='red')
            textlist[i].delete('1.0',END)
            textlist[i].insert(END,tmp,'a')
        showerror(title="ERROR",message="out of index")
    fcontent=open('./lib/content.txt','w')
    sys.stdout=fcontent
    if mystack.len>=1:
        text6.delete('1.0',END)
        ls(mystack.content[mystack.len-1-hand])
        fcontent.close()
        fcontent=open('./lib/content.txt','r')
        data=[line for line in fcontent.readlines()]
        i=0
        while i<len(data):
            text6.insert(END,data[i])
            text6.insert(END,'\n')
            i=i+1
        fcontent.close()
    else:
        text6.delete('1.0',END)
    f=open('/lib/log.txt','w')
    sys.stdout=f

def nextpacketlist():
    global hand
    if mystack.len>10:
        a=10
    else:
        a=mystack.len
    if 1<=hand and hand<=a:
        viewpacketlist()
        for i in range(4):
            tmp=textlist[i].get('1.0',END)
            textlist[i].delete('1.0',END)
            textlist[i].insert(END,tmp)
        if hand<a:
            hand=hand+1
        else:
            for i in range(4):
                tmp=textlist[4*(hand-1)+i].get('1.0',END)
                textlist[4*(hand-1)+i].tag_config('a',foreground='red')
                textlist[4*(hand-1)+i].delete('1.0',END)
                textlist[4*(hand-1)+i].insert(END,tmp,'a')
        for i in range(4):
            tmp=textlist[4*(hand-1)+i].get('1.0',END)
            textlist[4*(hand-1)+i].tag_config('a',foreground='red')
            textlist[4*(hand-1)+i].delete('1.0',END)
            textlist[4*(hand-1)+i].insert(END,tmp,'a')
    else:
        showerror(title="ERROR",message="out of index")
    fcontent=open('./lib/content.txt','w')
    sys.stdout=fcontent
    if mystack.len>=1:
        text6.delete('1.0',END)
        ls(mystack.content[mystack.len-1-hand])
        fcontent.close()
        fcontent=open('./lib/content.txt','r')
        data=[line for line in fcontent.readlines()]
        i=0
        while i<len(data):
            text6.insert(END,data[i])
            text6.insert(END,'\n')
            i=i+1
        fcontent.close()
    else:
        text6.delete('1.0',END)
    f=open('/lib/log.txt','w')
    sys.stdout=f


def viewpacketlist():
    weight=mystack.len/10
    for i in range(40):
        textlist[i].delete('1.0',END)
    for i in range(1,11):
        textlist[4*(i-1)].insert(END,i)
    i=1
    if mystack.len>=1:
        textlist[1].insert(END,mystack.content[mystack.len-1].src)
        textlist[2].insert(END,mystack.content[mystack.len-1].dst)
        textlist[3].insert(END,str(type(mystack.content[mystack.len-1])))
    while i<mystack.len and i<10:
        textlist[4*(i)+1].insert(END,mystack.content[mystack.len-i].src)
        textlist[4*(i)+2].insert(END,mystack.content[mystack.len-i].dst)
        textlist[4*(i)+3].insert(END,str(type(mystack.content[mystack.len-i])))
        i=i+1
    for i in range(4):
        tmp=textlist[i].get('1.0',END)
        textlist[i].tag_config('a',foreground='red')
        textlist[i].delete('1.0',END)
        textlist[i].insert(END,tmp,'a')

def sendfull():
    f=open('/lib/log.txt','w')
    sys.stdout=f
    if mystack.len>10:
        tmp=10
    else:
        tmp=len(mystack.content)
    for i in range(tmp):
        send(mystack.content[mystack.len-1-i])
    for i in range(tmp):
        mystack.Pop()
    viewpacketlist()
    Clear()
    text4.delete('1.0',END)
    text1.insert(END,"Packets have been sended...")
    text2.insert(END,"Packets have been sended...")
    text3.insert(END,"Packets have been sended...")
    text4.insert(END,"Packets have been sended...")
    text5.insert(END,"Packets have been sended...")


def callback():
    global mystack
    name= askopenfilename()
    a=rdpcap(name)
    i=0
    while i<len(a):
        mystack.Push(a[i])
        i=i+1
    viewpacketlist()







top=Tk()
top.title('phaX')
top.geometry('1200x700')

macda=StringVar()               #variables for layer2
macsa=StringVar()
ethertype=IntVar()

protocol = IntVar()                 #variables for layer3
TypeofService=IntVar()
Identification=IntVar()
Flag=IntVar()
Flagoff=IntVar()
TTL=IntVar()
SourceIp=StringVar()
DestinationIp=StringVar()

Protocol1=IntVar()            #variables for layer 4
TypeCode=IntVar()
SourcePort=IntVar()
DestPort=IntVar()
L4Flag=IntVar()
SeqNum=IntVar()
AckNum=IntVar()

text1,text2,text3,text4,text5,text6,textlist=Gui.mainframe(top=top,
          macda=macda,
          macsa=macsa,
          ethertype=ethertype,
          GenerateEther=GenerateEther,
          protocol=protocol,
          TypeofService=TypeofService,
          Identification=Identification,
          Flag=Flag,
          Flagoff=Flagoff,
          TTL=TTL,
          SourceIp=SourceIp,
          DestinationIp=DestinationIp,
          GeneratePkt=GeneratePkt,
          Protocol1=Protocol1,
          TypeCode=TypeCode,
          SourcePort=SourcePort,
          DestPort=DestPort,
          L4Flag=L4Flag,
          SeqNum=SeqNum,
          GenerateSegment=GenerateSeg,
          Clear=Clear,
          Generate=Generate,
          deletepacketlist=deletepacketlist,
          previouspacketlist=previouspacketlist,
          nextpacketlist=nextpacketlist,
          viewpacketlist=viewpacketlist,
          sendfull=sendfull,
          callback=callback)

text4.tag_config('a',foreground='gray')
s="input something...."
text4.insert(END,s,'a')


mainloop()