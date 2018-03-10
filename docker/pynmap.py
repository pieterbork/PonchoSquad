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

def getRoomID(api, roomName):
    rawRooms=api.rooms.list()
    rooms=[room for room in rawRooms if room.title == roomName]
    if len(rooms) == 0:
        api.rooms.create(roomName)
    for room in rooms:
        roomID=(room.id)
        return roomID


nm = nmap.PortScanner()
nm.scan(hosts='10.202.0.0/24', arguments='oX - -p 22-443')
roomID=getRoomID(api,roomName)
roomID = "Y2lzY29zcGFyazovL3VzL1JPT00vMTYwZGM5NjAtMjQ4Ni0xMWU4LTk1ZGItZTk5NmY0ZDIyYzcw"
api.messages.create(roomID, text="Scan Results:")

for host in nm.all_hosts():
	# send message
	api.messages.create(roomID, text="Host: %s (%s)" % (host,nm[host].hostname()))
	print ('------------------')
	print ('Host: %s (%s)' % (host,nm[host].hostname()))
