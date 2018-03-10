#!/usr/bin/env python3
#Joe's example code for sending bash commands from a spark room
import subprocess
from ciscosparkapi import CiscoSparkAPI

import configparser
import time
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='A program to receive messages from Cisco Spark on Omega')
parser.add_argument('--pid', help="Create a pid file in /var/run/a01.pid",  action="store_true")
args=parser.parse_args()

if args.pid:
        print("Creating PID file.")
        fh=open("/var/run/sparkRun.pid", "w")
        fh.write(str(getpid()))
        fh.close()

#read API key
config= configparser.ConfigParser()
#config.read('/root/spark.cfg')
#apiKey=config['apiKey']['key']
#apiKey="NmZiNGU3NWYtNWY3My00MzI1LWE5MzUtODFmMmY5MGZmYmU3MWFkODIxMDgtODQ0"
apiKey="YTM4ZDk2NjAtNTA3Zi00ZTVkLWFjMjgtZjIwNzMxYjZjM2JjNDFhZmIwZDgtNzM4"

api = CiscoSparkAPI(access_token=apiKey)
roomName="darkmatter"

def getRoomID(api, roomName):
        rawRooms=api.rooms.list()
        rooms=[room for room in rawRooms if room.title == roomName]
        if len(rooms) == 0:
                print("No roomID found.")
                quit()
        else:
                for room in rooms:
                        roomID=(room.id)
        if len(rooms) > 1:
                print("Found multiple rooms with name {} , using newest room.\n -You may want to delete some of the rooms".format(roomName))

        return roomID

roomID=getRoomID(api, roomName)
#subprocess.Popen("oled-exp scroll left", shell=True, stdout=subprocess.PIPE)
lastMessageID=''
lastMessageTime=datetime.now()
while True:
        try:
                messages = api.messages.list(roomID)
        except:
                messages()
        for message in messages:
                if message.text[:3] == "run":
                        messageTime=(message.created.split(".")[0])
                        messageTime=datetime.strptime(messageTime, '%Y-%m-%dT%H:%M:%S')
                        if message.id != lastMessageID and messageTime > lastMessageTime:
                                command=message.text[3:]
                                oledMsg="Command: " + command
                                oledMsg="oled-exp -i -c write \"{}\"".format(oledMsg)
                                sendMsg=(subprocess.Popen(oledMsg, shell=True, stdout=subprocess.PIPE).stdout.read()).strip()
                                commandOutput=subprocess.getoutput(command)
                                api.messages.create(roomID,text="Output: \n" + commandOutput)

                                lastMessageID=message.id
                                lastMessageTime=messageTime
                                break
        time.sleep(30)
