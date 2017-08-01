# -*- coding: utf-8 -*-
import IPy
ip4 = IPy.IP('10.0.0.0/30')
ip6 = IPy.IP('::1')
print ip4.version()
print ip6.version()
print ip4.len()

for x in ip4:
    print x
ip = IPy.IP('8.8.8.8')
print ip.reverseNames()
print ip.iptype()
print ip.int()
print ip.strHex()
print ip.strBin()
print IPy.IP(0x8080808)
print IPy.IP('192.168.1.0').make_net('255.255.255.0')
print IPy.IP('192.168.1.0/24').strNormal(0)
print IPy.IP('192.168.1.0/24').strNormal(1)
print IPy.IP('192.168.1.0/24').strNormal(2)
print IPy.IP('192.168.1.0/24').strNormal(3)
print '10.0.0.100' in IPy.IP('10.0.0.0/24')
print IPy.IP('10.0.0.0/24') in IPy.IP('10.0.0.0/16')
print IPy.IP('192.168.0.0/23').overlaps('192.168.1.0/24')

print ip.net()
print ip.netmask()
print ip.broadcast()
print ip.reverseName()[0]
#IP int 转化
print IPy.IPint('8.8.8.8',4).int()
print IPy.intToIp(134744072,4)