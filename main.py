###                                           ###
#   SIMPLE NETWORK MONITOR/DIAGNOSTIC TOOL :3   #
###                                           ###

import os
import socket
import subprocess

def ping():
    host = input("Please enter ip of the host for ping")
    os.system(f"ping -c 4 {host}")
def traceroute():
    dest = input("Please enter destination for traceroute")
    os.system(f"traceroute{dest}")
def dns():
    domain = input("Please enter domain to lookup")
    os.system(f"nslookup {domain}")
def port_scan():
    host = input("Please enter host ip for port scan")
    port_range = input("Please enter the range for port scan eg. 20-100")
    os.system(f"nmap -p {port_range} {host}")
def check_net():
    try:
        socket.create_connection(("www.google.com", 80))
        print("Internet is avalable")
    except OSError:
        print("No internet avalable")
ping()