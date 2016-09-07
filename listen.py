#!/usr/bin/python2
# -*- coding: utf-8 -*-
from scapy.all import sniff, ARP


def arp_received(packet):
    if packet[ARP].op == 1 and packet[ARP].hwdst == '00:00:00:00:00:00':
        if packet[ARP].hwsrc == '50:f5:da:6f:98:6c':  # This is the MAC of the first dash button
            print("Button pressed!")
        elif packet[ARP].hwsrc != 'b8:27:eb:17:d5:22':  # If it is not the MAC of the Raspi it could be another button
            print("Unknown Device connecting: " + packet[ARP].hwsrc)


if __name__ == "__main__":
    print("Listening for ARP packets...")
    sniff(prn=arp_received, iface="wlan0", filter="arp")
