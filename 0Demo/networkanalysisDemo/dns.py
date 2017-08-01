# -*- coding: utf-8 -*-
import pcap,dpkt
pc = pcap.pcap()
#We'll start off by setting pypcap's BPF expression to "udp dst port 53" 
pc.setfilter('tcp port 80')

for ts, pkt in pc:
    eth = dpkt.ethernet.Ethernet(pkt)
    ip = eth.data
    tcp = ip.data

    print tcp.sport
    print tcp.dport
    if tcp.dport == 80 and len(tcp.data) > 0:
        http = dpkt.http.Request(tcp.data)
        #Once the HTTP payload has been parsed, we can examine its various attributes
        print http.method
        print http.uri
        print http.version
        print http.headers['user-agent']


