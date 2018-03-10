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
    print(url)
    if values:
        r = requests.post(url, data=json.dumps(values), headers=headers)
    else:
        r = requests.get(url, headers=headers)
    return r.text

def investigate_domain(domain):
    url = 'https://investigate.api.opendns.com/security/name/{}.json'.format(domain)
    url = 'https://investigate.api.opendns.com/domains/{}/latest_tags'.format(domain)
    url = 'https://investigate.api.umbrella.com/timeline/{}'.format(domain)
    print(url)
    resp = get_response(url)
    print("investigate", resp)


investigate_domain("www.ncicye.com")
investigate_domain("www.dreamscreen.xyz")
investigate_domain("www.internetbadguys.com")
investigate_domain("www.ciilhk.com")

resp = get_response('https://investigate.api.opendns.com/domains/categorization/amazon.com')
print(resp)

values = ["google.com", "yahoo.com"]
resp = get_response('https://investigate.api.opendns.com/domains/categorization/', values)
print("domain categorization", resp)

resp = get_response('https://investigate.api.opendns.com/domains/categories')
print("domain categories", resp)

resp = get_response('https://investigate.api.opendns.com/domains/score/example.com')
print("domain score", resp)

resp = get_response('https://investigate.api.opendns.com/domains/score/', values)
print("domain score", resp)

resp = get_response('https://investigate.api.opendns.com/security/name/www.internetbadguys.com.json')
print("security", resp)

resp = get_response('https://investigate.api.opendns.com/domains/www.internetbadguys.com/latest_tags')
print("domain investigate", resp)

resp = get_response('https://investigate.api.opendns.com/dnsdb/name/a/homestarrunner.com.json')
print("dnsdb", resp)

resp = get_response('https://investigate.api.opendns.com/ips/173.255.113.232/latest_domains')
print("latest domain", resp)

