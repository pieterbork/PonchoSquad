#!/usr/bin/python
from flask import Flask, render_template, request, redirect, session, flash
import json
from call_examples import investigate_domain,get_vt_report
from ciscosparkapi import CiscoSparkAPI
from configparser import ConfigParser
app = Flask(__name__)

config = ConfigParser()
config.read('spark.cfg')
botkey = config['spark']['botkey']
apikey = config['spark']['apikey']
roomID = config['spark']['roomId']

botapi = CiscoSparkAPI(access_token=botkey)
api = CiscoSparkAPI(access_token=apikey)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		if request.headers['Host'] == "6d84a76b.ngrok.io" and request.headers['User-Agent'] == "Squared Scheduler/1.0":
			messages = api.messages.list(roomID)
			lastmessage = ""
			for message in messages:
				lastmessage = message.text
				break
			print(lastmessage)
			if "investigate" in lastmessage:
				domain = lastmessage.split()[1]
				domain_is_bad = investigate_domain(domain)
				vt_1, vt_2 = get_vt_report(domain)
				print(domain_is_bad, vt_1, vt_2)
				if domain_is_bad:
					botapi.messages.create(roomID, markdown="<h1>Bad Domain</h1><hr>")
					botapi.messages.create(roomID, markdown="Umbrella Alerts: " + ", ".join(domain_is_bad))
					botapi.messages.create(roomID, markdown="VirusTotal Sources Confirmed: " + ", ".join(vt_2))
					botapi.messages.create(roomID, markdown="From: " + ", ".join(vt_1))
					botapi.messages.create(roomID, markdown="<hr>")
				else:
					botapi.messages.create(roomID, markdown="<h1>No Issues Found!</h1><hr>")
			return "Success"
		else:
			return "Unauthorized"
	else:
		return "Home";

@app.route('/manual', methods=['POST'])
def manual():
    if request.method == "POST":
        if request.headers['Host'] == "6d84a76b.ngrok.io" and request.headers['User-Agent'] == "Squared Scheduler/1.0":
            domain = json.loads(request.data)['url']
            domain_is_bad = investigate_domain(domain)
            vt_1, vt_2 = get_vt_report(domain)
            print(domain_is_bad, vt_1, vt_2)
            if domain_is_bad:
                    botapi.messages.create(roomID, markdown="<h1>Bad Domain from cURL</h1><hr>")
                    botapi.messages.create(roomID, markdown="Domain: {}".format(domain.replace('.', '[.]')))
                    botapi.messages.create(roomID, markdown="Umbrella Alerts: " + ", ".join(domain_is_bad))
                    botapi.messages.create(roomID, markdown="VirusTotal Sources Confirmed: " + ", ".join(vt_2))
                    botapi.messages.create(roomID, markdown="From: " + ", ".join(vt_1))
                    botapi.messages.create(roomID, markdown="<hr>")
                    return "Bad"
            else:
                    return "Good"
            print(url)
        else:
            return "Unauthorized"
    else:
        return "Manual";


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
