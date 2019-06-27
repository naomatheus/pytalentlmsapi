from flask import jsonify, Blueprint
import json
from flask_restful import (Resource, Api, reqparse, url_for)
import config
import requests
from requests.auth import HTTPBasicAuth

## both of these classes are inherited from the Resource
## because we're importing from flask_restful, classes are given resource, resource enables the classes to handle all HTTP request and response methods

## Setting up View Functions

## Setting up third party api requests

## New Forms of Authentication
#https://2.python-requests.org/en/master/user/authentication/



class myAuth(Resource, requests.auth.AuthBase):
	## must call Resource as part of class
	def __call__(self, r):
		def __init__(self):

		#implement the authentication required
			super().__init__()

	def get(self):
		try: 
			print('calling authbase.py route')

			lms_header = {'user':config.api_key,'password':'','setApiKey':config.api_key,'setDomain':config.home_domain,'content-type':'application/json'}
			headers = lms_header
			print(headers, '<-- HTTP Basic headers')

			req = requests.get('https://allchicago.talentlms.com/api/v1/users', headers=headers, auth=HTTPBasicAuth(config.api_key,''))
			res = req.text
			status = req.status_code
			print('request successful')
			json_res = json.dumps(res)
			## json dump to pythor str obj
			json_loaded_res = json.loads(res)
			## load response as json
			return json_loaded_res, status
		except:
			print('hit exception')
			return Exception

	

auth_api = Blueprint('resources.auth_api', __name__)
api = Api(auth_api)
api.add_resource(
	myAuth,
	'/users',
	endpoint='users'
)