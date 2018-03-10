#!/usr/bin/python
import requests
import json
import os, sys

def get_response(url, values=None, headers=None, params=None):
    print(url)
    if values:
        r = requests.post(url, data=json.dumps(values), headers=headers)
    elif params:
        r = requests.post(url, params=params, headers=headers)
    else:
        r = requests.get(url, headers=headers)
    return r.text

def investigate_domain(domain):
    token = "7be254dc-9e39-4d06-b729-3578827b20db"
    spark_headers = {
      'Authorization': 'Bearer ' + token
    }
    url = 'https://investigate.api.umbrella.com/timeline/{}'.format(domain)
    resp = get_response(url, headers=spark_headers)
    info = json.loads(resp)
    categories = info[0]['categories']
    ret_str = "The Umbrella API reports "
    if len(categories) > 0:
        ret_str += ", ".join(categories)
    else:
        ret_str += "that url is clean"

    return ret_str

def get_vt_report(domain):
    vt_headers = {
        "Accept-Encoding": "gzip, deflate",
        "User-Agent" : "gzip,  My Python requests library example client or username"
    }
    vtparams = {'apikey': '4837b1adf0d071cd02bd05953d59b3e20ff48bcccea185b37f2bc2a63fcc73d7', 'resource':domain}
    resp = get_response('https://www.virustotal.com/vtapi/v2/url/report', params=vtparams, headers=vt_headers)
    info = json.loads(resp)
    scans = info['scans']

    results = {"sources": set([]), "types": set([])}
    for scan in scans:
        detected = scans[scan]['detected']
        result = scans[scan]['result']
        if detected:
            results["sources"].add(scan)
            results["types"].add(result)
#                print("{} Reported this as {}".format(scan, result))
    ret_str = "VirusTotal sources confirmed [{}] from [{}]".format(", ".join(results["types"]),", ".join(results["sources"]))
    return ret_str



#investigate_domain('google.com')
#investigate_domain("www.ncicye.com")
#investigate_domain("www.dreamscreen.xyz")
#investigate_domain("www.internetbadguys.com")
#investigate_domain("www.ciilhk.com")
#
#resp = get_response('https://investigate.api.opendns.com/domains/categorization/amazon.com')
#print(resp)

#values = ["google.com", "yahoo.com"]
#
##nasty domains
#value = "fbl.com.sg"
#value = "wd4o.com"
#
#results = get_vt_report(value)
#print(results)
#print("MAH RESULTS", results)
#
#domain_is_bad = investigate_domain(value)
#print(domain_is_bad)
#if domain_is_bad:
#    #POST TO SPARK ROOM
#    print("Ohhh boi bad domain")
#quit()
#
#resp = get_response('https://investigate.api.opendns.com/domains/categories')
#print("domain categories", resp)
#
#resp = get_response('https://investigate.api.opendns.com/domains/score/example.com')
#print("domain score", resp)
#
#resp = get_response('https://investigate.api.opendns.com/domains/score/', values)
#print("domain score", resp)
#
#resp = get_response('https://investigate.api.opendns.com/security/name/www.internetbadguys.com.json')
#print("security", resp)
#
#resp = get_response('https://investigate.api.opendns.com/domains/www.internetbadguys.com/latest_tags')
#print("domain investigate", resp)
#
#resp = get_response('https://investigate.api.opendns.com/dnsdb/name/a/homestarrunner.com.json')
#print("dnsdb", resp)
#
#resp = get_response('https://investigate.api.opendns.com/ips/173.255.113.232/latest_domains')
#print("latest domain", resp)
#
