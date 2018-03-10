#!/usr/bin/env python3
import os, sys
import requests
import json

url = sys.argv[-1]
headers = {'Host': '6d84a76b.ngrok.io', 'User-Agent': 'Squared Scheduler/1.0'}

payload = {'url': url}

r = requests.post('https://6d84a76b.ngrok.io/manual', headers=headers, data=json.dumps(payload))

if r.text == 'Good':
    print("curl {}".format(sys.argv[1::]))
else:
    print("Bad domain, aborting cURL")
