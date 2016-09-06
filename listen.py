#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from scapy.all import sniff, ARP


def arp_received(packet):
    if packet[ARP].op == 1 and packet[ARP].psrc == '0.0.0.0':
        print(packet[ARP].hwsrc)


if __name__ == "__main__":
    print("Listening for ARP packets...")
    print(sniff(prn=arp_received, filter="arp", store=0))
