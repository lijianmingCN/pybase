import dpkt,random,binascii,socket

#To create the Echo payload, we simple create an instance of the Echo class
echo = dpkt.icmp.ICMP.Echo()
echo.id = random.randint(0, 0xffff)
echo.seq = random.randint(0, 0xffff)
echo.data = 'hello world'
print binascii.hexlify(str(echo))

#Next, we create the ICMP payload and assign its attributes
icmp = dpkt.icmp.ICMP()
icmp.type = dpkt.icmp.ICMP_ECHO
icmp.data = echo
print binascii.hexlify(str(icmp))

#Now that we have the full binary payload of our ICMP packet (str(icmp)), we can send it out via a standard ICMP socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, dpkt.ip.IP_PROTO_ICMP)
s.connect(('8.8.8.8', 1))
sent = s.send(str(icmp))

print 'sent %d bytes' % sent

