from ciscosparkapi import CiscoSparkApi

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

# send message
roomID=getRoomID(api,roomName)
api.messages.create(roomID, text="Hello")

tempID=[]

# read in messages
messages = api.messages.list(roomID)
for message in messages:
    tempID.append(message.id)


while True:
    messages = api.messages.list(roomID)
    for message in messages:
        if message.id not in tempID:
            tempID.append(message.id)
            print(message.text)
            if message.text == "fetch":
                api.messages.create(roomID, text="hi")
            elif message.text == "order pizza":
                api.messages.create(roomID, text="ERROR: Insufficient funds in banking account.")
            elif message.text == "what's my password?":
                api.messages.create(roomID, text="goochipoodle")
    time.sleep(1)
