import re

def MacCheck(mac):
    patt='([0-9a-fA-F]{2}:){5}([0-9a-fA-F]{2})'
    a=re.match(patt,mac)
    if a is not None:
        return 1
    else:
        return 0

def IpCheck(ip):
    patt='^([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])'
    a=re.match(patt,ip)
    if a is not None:
        return 1
    else:
        return 0

def TTLCheck(ttl):
    if (ttl>0)and(ttl<=255):
        return 1
    else:
        return 0

def PortCheck(port):
    if (port>0)and(port<=65535):
        return 1
    else:
        return 0

def icmptypecheck(typecode):
    a=[0,3,4,5,8,11,12,13,14,15]
    if typecode in a:
        return 1
    else:
        return 0