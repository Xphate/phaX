import BuildPacket

def GenerateEther(macda,macsa,ethertype):
    frame=etherframe(macda,macsa,ethertype)
    frame.buildetherframe()
    return frame

def GeneateipPkt(tos,id,flags,fragoffset,ttl,sourceip,destinationip,ethe,text):
    pkt=ippacket(tos,id,flags,fragoffset,ttl,sourceip,destinationip,ether)
    pkt.buildippacket()
    return pkt

def GeneratearpPkt():
    return

def GenerateTCP():
    return

def GenerateUDP():
    return
