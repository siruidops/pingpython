#!/usr/bin/env python
# TheHackings
# Author: SirUidops

import sys
import socket
from scapy.all import *

ip = raw_input(" >>> ")

try:
	ip = socket.gethostbyname(ip)
except:
	print "Host Is Down"
	sys.exit()

icmp = IP(dst=ip)/ICMP()
resp = sr1(icmp, timeout=10)

if str(resp).upper == "NONE":
	print "Host Is Down"
else:
	print "Host Is Up"
