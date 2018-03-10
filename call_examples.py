#!/usr/bin/python
import requests
import json
import os, sys

token = os.getenv('INVESTIGATE_TOKEN', False)
token = "3bb69d0a-ccc7-40b5-a386-48632333e381"

if not token:
  print("ERROR: environment variable \'INVESTIGATE_TOKEN\' not set. Invoke script with \'INVESTIGATE_TOKEN=%YourToken% python scripts.py\'")
  sys.exit(1)

# domains/categorization

headers = {
  'Authorization': 'Bearer ' + token
}

def get_response(url, values=None):
    if values:
        r = requests.post(url, data=json.dumps(values), headers=headers)
    else:
        r = requests.get(url, headers=headers)
    return r.text


resp = get_response('https://investigate.api.opendns.com/domains/categorization/amazon.com')
print(resp)

values = ["google.com", "yahoo.com"]
resp = get_response('https://investigate.api.opendns.com/domains/categorization/', values)
print(resp)

resp = get_response('https://investigate.api.opendns.com/domains/categories')
print(resp)

resp = get_response('https://investigate.api.opendns.com/domains/score/example.com')
print(resp)

resp = get_response('https://investigate.api.opendns.com/domains/score/', values)
print(resp)

