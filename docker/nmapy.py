#! /usr/local/bin/python
from ciscosparkapi import CiscoSparkAPI
import configparser
import nmap 
import time
#print('imported!')

# read config file
config = configparser.ConfigParser()
config.read('api.cfg')
apikey = config['api']['botkey']
api = CiscoSparkAPI(access_token=apikey)
roomName = "Poncho Squad"

roomID = "Y2lzY29zcGFyazovL3VzL1JPT00vMTYwZGM5NjAtMjQ4Ni0xMWU4LTk1ZGItZTk5NmY0ZDIyYzcw"
api.messages.create(roomID, text="Scanning Domain: nmap.org...")

nm = nmap.PortScanner()
nm.scan(hosts='nmap.org', arguments='-p 22-443')


for host in nm.all_hosts():
	# send message
	api.messages.create(roomID, text=("Host: %s (%s)" % (host,nm[host].hostname())))
	api.messages.create(roomID, text=('------------------'))
	api.messages.create(roomID, text=('Host: %s (%s)' % (host,nm[host].hostname())))
	api.messages.create(roomID, text=('State: %s ' % nm[host].state()))
	for proto in nm[host].all_protocols():
	    api.messages.create(roomID, text=('-----------'))
	    api.messages.create(roomID, text=('Protocol %s' % proto))
	    lport = nm[host][proto].keys()

	    lport.sort()
	    for port in lport:
	        api.messages.create(roomID, text=('port : %s\tstate : %s' % (port, nm[host][proto][port]['state'])))

