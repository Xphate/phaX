import sys
from scapy.all import *

class etherframe:
    def __init__(self,macda,macsa,ethertype):
        self.dst=macda
        self.src=macsa
        self.type=ethertype
    def buildetherframe(self):
        self.frame=Ether(dst=self.dst,src=self.src,type=self.type)
    def sendetherframe(self):
        send(self.frame)

class arppacket:
    def __init__(self,op,hwsrc,psrc,pdst,ether):
        self.op=op
        self.hwsrc=hwsrc
        self.psrc=psrc
        self.pdst=pdst
        self.ether=ether

    def buildarppacket(self):
        self.pkt=self.ether.frame/ARP(op=self.op,
                                hwsrc=self.hwsrc,
                                psrc=self.psrc,
                                pdst=self.pdst)

    def sendarppacket(self):
        send(self.pkt)

class ippacket:
    def __init__(self,tos,id,flags,fragoffset,ttl,sourceip,destinationip,ether):
        self.tos=tos
        self.id=id
        self.flags=flags
        self.frag=fragoffset
        self.ttl=ttl
        self.src=sourceip
        self.dst=destinationip
        self.ether=ether
    def buildippacket(self):
        self.pkt=self.ether.frame/IP(tos=self.tos,
                    id=self.id,
                    flags=self.flags,
                    frag=self.frag,
                    ttl=self.ttl,
                    src=self.src,
                    dst=self.dst)
    def send(self):
        send(self.pkt)
