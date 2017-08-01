# -*- coding: utf-8 -*-
#Use DPKT to read in a pcap file and print out the contents of the packets
import dpkt
import datetime
import socket
import binascii

def mac_addr(mac_string):
    return ':'.join('%02x' % ord(b) for b in mac_string)

def ip_to_str(address):
    return socket.inet_ntop(socket.AF_INET, address)

#Args: pcap: dpkt pcap reader object (dpkt.pcap.Reader)
def print_packets(pcap):
    # For each packet in the pcap process the contents
    for timestamp, buf in pcap:
        # Print out the timestamp in UTC
        print 'Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp))

        # Unpack the Ethernet frame (mac src/dst, ethertype)
        eth = dpkt.ethernet.Ethernet(buf)
        print 'Ethernet Frame: ', mac_addr(eth.src), mac_addr(eth.dst), eth.type

        # Make sure the Ethernet frame contains an IP packet
        # EtherType (IP, ARP, PPPoE, IP6... see http://en.wikipedia.org/wiki/EtherType)
        if eth.type != dpkt.ethernet.ETH_TYPE_IP:
            print 'Non IP Packet type not supported %s\n' % eth.data.__class__.__name__
            continue

        # Now unpack the data within the Ethernet frame (the IP packet) 
        # Pulling out src, dst, length, fragment info, TTL, and Protocol
        ip = eth.data

        # Pull out fragment information (flags and offset all packed into off field, so use bitmasks)
        do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
        more_fragments = bool(ip.off & dpkt.ip.IP_MF)
        fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

        # Print out the info
        print 'IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d)\n' % \
              (ip_to_str(ip.src), ip_to_str(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments, fragment_offset)
        
        #As we can see from the output, eth is the Ethernet object, pkt.data is the IP object, and pkt.data.data is the TCP object.
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
        
        
        
def test():
    """Open up a test pcap file and print out the packets"""
    with open('data/http.pcap') as f:
        pcap = dpkt.pcap.Reader(f)
        print_packets(pcap)


if __name__ == '__main__':
    test()