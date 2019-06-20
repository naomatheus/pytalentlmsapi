from flask import Flask, g, jsonify
from flask_cors import CORS
# import models
# from resources.api import talentlms_api
import requests

import config

HOST='0.0.0.0'

app = Flask(__name__)

r = requests.get('https://jobs.github.com/positions.json?description=python&location=new+york')

lms_header = {'setApiKey':config.api_key,'setDomain':config.home_domain,'content-type':'application/json'}

@app.before_request
def before_request():
	print('request beginning')


@app.after_request
def after_request(response):
	print('response received')
	return response


@app.route('/api')
def api_call():
	
	try: 
		setApiKey()
		return 'hi, successful try' 
	except err
		return err
	


	

if __name__ == '__main__':
	app.run(debug=config.DEBUG,port=config.PORT)
