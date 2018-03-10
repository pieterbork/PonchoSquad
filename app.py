#!/usr/bin/python
from flask import Flask, render_template, request, redirect, session, flash
import json
from ciscosparkapi import CiscoSparkAPI
from configparser import ConfigParser
app = Flask(__name__)

config = ConfigParser()
config.read('spark.cfg')
apikey = config['spark']['apikey']
roomID = config['spark']['roomID']

api = CiscoSparkAPI(access_token=apikey)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		if request.headers['Host'] == "3af1397b.ngrok.io" and request.headers['User-Agent'] == "Squared Scheduler/1.0":
			messages = api.messages.list(roomID)
			lastmessage = ""
			for message in messages:
				lastmessage = message.text
				break
			return "Success"
		else:
			return "Unauthorized"
	else:
		return "Home";

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
