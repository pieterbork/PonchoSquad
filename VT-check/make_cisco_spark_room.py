#!/usr/bin/env python3
from ciscosparkapi import CiscoSparkAPI

#apiKey="NmZiNGU3NWYtNWY3My00MzI1LWE5MzUtODFmMmY5MGZmYmU3MWFkODIxMDgtODQ0"
apiKey="YTM4ZDk2NjAtNTA3Zi00ZTVkLWFjMjgtZjIwNzMxYjZjM2JjNDFhZmIwZDgtNzM4"
api = CiscoSparkAPI(access_token=apiKey)

# Find all rooms that have 'ciscosparkapi Demo' in their title
all_rooms = api.rooms.list()
demo_rooms = [room for room in all_rooms if 'foo' in room.title]

# Delete all of the demo rooms
for room in demo_rooms:
    api.rooms.delete(room.id)

# Create a new demo room
demo_room = api.rooms.create('darkmatter')

# Add people to the new demo room
#email_addresses = [""]
#for email in email_addresses:
#    api.memberships.create(demo_room.id, personEmail=email)

# Post a message to the new room, and upload a file
api.messages.create(demo_room.id, text="Embrace The Void...")
