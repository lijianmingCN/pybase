# -*- coding: utf-8 -*-
import pcap

devs = pcap.findalldevs()
print devs

p = pcap.pcap('en0')
print p.name
print p.filter