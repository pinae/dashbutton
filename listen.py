#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from scapy.all import sniff, ARP


def arp_received(packet):
    if packet[ARP].hwsrc == '50:f5:da:6f:98:6c':
        print("Button pressed!")
    else:
        print(packet[ARP].hwsrc)


if __name__ == "__main__":
    print("Listening for ARP packets...")
    sniff(prn=arp_received, iface="wlan0", filter="arp")
