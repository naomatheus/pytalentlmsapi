from flask import Flask, g, jsonify
from flask_cors import CORS
# import models
# from resources.api import talentlms_api
import requests

import config
from resources.authbase import auth_api
from resources.users import users_api

HOST='0.0.0.0'

app = Flask(__name__)

app.register_blueprint(auth_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')

lms_header = {'user':config.api_key,'password':'','setApiKey':config.api_key,'setDomain':config.home_domain,'content-type':'application/json'}

@app.before_request
def before_request():
	print('request beginning')


@app.after_request
def after_request(response):
	print('response received')
	return response


@app.route('/')
def api_call():
	
	try: 
## this section is to test the flask server2
		# req = requests.get('https://jobs.github.com/positions.json?description=python&location=new+york')
		
		# res = req.json()
		# print(res)
		# jsonRes = jsonify(res)
		# return jsonRes
## this section is to test the flask server 
		headers = lms_header
		print(headers, '<-- headers')
		req = requests.get('https://allchicago.talentlms.com/api/v1/users', headers=headers)

		res = req.text
		status = req.status_code


		return 'successful call using authbase class'

	except: 
		return 'there was an issue'
	


	

if __name__ == '__main__':
	app.run(debug=config.DEBUG,port=config.PORT)
