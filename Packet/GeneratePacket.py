"""
from GUI import Gui
from Packet import PacketCode
from Tkinter import *
from lib import InputCheck
from tkMessageBox import *
from scapy.all import *
import sys
from lib import Stack

def ViewEther(full):
    global text1
    text1.delete('1.0',END)
    newstring="src: "+full.src+'\n'+"dst: "+full.dst+'\n'+"type: "+str(full.type)+'\n'
    text1.tag_config('a',foreground = 'red')
    text1.insert(END,"####[ Ethernet ]####\n",'a')
    text1.tag_config('b',foreground='blue')
    text1.insert(END,newstring,'b')


def ViewPkt(full):
    global text2
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

"""