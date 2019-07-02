from flask import Flask, g, jsonify
from flask_cors import CORS
## Flask is the microframework for constructing a server to make/handle HTTP Requests
import requests
## Requests module handles sending/receiving HTTP Requests (google python requests)

import config
# config is short for config.py file. This holds environment variables and hides them if git ignored (in .gitignore file)
## this way the API KEY and domain for All Chicago LMS is hidden from public repositories
from resources.authbase import auth_api
from resources.users import users_api
from resources.edit_users import edit_users_api
## Resource imports come from the controller files. These route the HTTP requests

HOST='0.0.0.0'

app = Flask(__name__)
## Flask object is assigned to app

app.register_blueprint(auth_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')
app.register_blueprint(edit_users_api, url_prefix='/api/v1')
# blueprint registers the url prefix for any controllers connected to server

lms_header = {'user':config.api_key,'password':'','setApiKey':config.api_key,'setDomain':config.home_domain,'content-type':'application/json'}
# lms header contains authentication information

@app.before_request
def before_request():
	print('request beginning')


@app.after_request
def after_request(response):
	print('response received')
	return response

# This commented block is not in use
# @app.route('/')
# def api_call():
	
# 	try: 
# ## this section is to test the flask server2
# 		# req = requests.get('https://jobs.github.com/positions.json?description=python&location=new+york')
		
# 		# res = req.json()
# 		# print(res)
# 		# jsonRes = jsonify(res)
# 		# return jsonRes
# ## this section is to test the flask server 
# 		headers = lms_header
# 		print(headers, '<-- headers')
# 		req = requests.get('https://allchicago.talentlms.com/api/v1/users', headers=headers)

# 		res = req.text
# 		status = req.status_code


# 		return 'successful call using authbase class'

# 	except: 
# 		return 'there was an issue'
	


## if the server exists, run it on the port in .config, tells the local server where to run

if __name__ == '__main__':
	app.run(debug=config.DEBUG,port=config.PORT)
