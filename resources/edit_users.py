from flask import jsonify, Blueprint, abort, make_response, request
from flask_restful import (Resource, Api, reqparse, inputs, fields, marshal, marshal_with, url_for)
import json
import config
import requests
from requests.auth import HTTPBasicAuth
## importing objects from Flask, and using requests for Basic HTTP Authorization (Google Basic HTTP)

class EditUsers(Resource, requests.auth.AuthBase):
	# this class is the controller, it contains all methods needed
	def __init__(self):
		# RequestParser (reqparse) is a flask library that let's you send many types of data along with an HTTP request
		self.reqparse = reqparse.RequestParser()
		# self.reqparse.add_argument(
		# 	# the add_argument method converts form data into objects that are usable within the code (args) 
		# 	'username',
		# 	required=True,
		# 	help='no username provided',
		# 	location=['form','json']
		# )
		# self.reqparse.add_argument(
		# 	'login',
		# 	required=False,
		# 	help='no login provided',
		# 	location=['form','json']
		# )
		self.reqparse.add_argument(
			'email',
			required=False,
			help='not an email',
			location=['form','json']
		)
		self.reqparse.add_argument(
			'user_id',
			required=False,
			help='no id',
			location=['form','json']
		)
		self.reqparse.add_argument(
			'bio',
			required=False,
			help='bad bio',
			location=['form','json']
		)

		super().__init__()

	def get(self):
		try:
			print('calling get a single user in edit_users.py')

			lms_header = {'user':config.api_key,'password':'','setApiKey':config.api_key, 'setDomain':config.home_domain, 'content-type':'multipart/form-data'}

			headers = lms_header

			args = self.reqparse.parse_args()
			#arguments from the form, translated by reqparse 
			print(args,'<-- args as dict')
			print(args.user_id, '<--- the user_id')
			print(args.email,'<-- users email')
			# get_req = requests.get('https://allchicago.talentlms.com/api/v1/users/id:'+args.user_id, headers=headers, auth=HTTPBasicAuth(config.api_key,''))
			get_req = requests.get('https://allchicago.talentlms.com/api/v1/users/email:'+args.email, headers=headers, auth=HTTPBasicAuth(config.api_key,''))
			get_res = get_req.text

			print(get_res,'<-- the get response')
			
			json_get_res = json.loads(get_res)
			return json_get_res

		except:
			print('hit exception')
			return Exception

	def post(self):
		## this class can receive post requests
		try:
			print('hitting edit users route in edit_users.py')

			lms_header = {'user':config.api_key,'password':'','setApiKey':config.api_key, 'setDomain':config.home_domain, 'content-type':'application/json'}

			headers = lms_header

			#remove null values, only send non-null values with payload

			payload = self.reqparse.parse_args()
			#arguments from the form, translated by reqparse 
			
			
			payload_list = []
			payload_list.append(payload)
			print(payload_list,'<-- payload list')
			json_payload = json.dumps(payload)
			print(json_payload, '<-- json payload`')

			# Send a post request to All Chicago's LMS, use our apikey and domain in headers, use basic http authorization, and send the arguments from the form as the data object in the request 
			## a data object is typically sent with a post request 

			# call get user by id to verify their id
			get_req = requests.get('https://allchicago.talentlms.com/api/v1/users/email:'+payload.email, headers=headers,auth=HTTPBasicAuth(config.api_key,''))

			get_res = get_req.text
			print(get_res,  '<-- get response of post route')
			## the get response returns a string object (JSON approximation)
			print(json.loads(get_res),'<-- the json loaded string')
			print(type(json.loads(get_res)),'<-- type of the json loaded string')

			response_dict = json.loads(get_res)
			print(response_dict["id"],'<--- id of the dictionary of json loaded get res')
			user_id = response_dict["id"]
			
			# use that id in the payload of the POST request
			
			res = requests.post('https://allchicago.talentlms.com/api/v1/edituser', headers=headers, auth=HTTPBasicAuth(config.api_key,''),data=user_id)
			# ## need another way to provide the arguments for this to work

			response = res.text
			print(response,'<-- valid response from requests.post')

			# json_res = json.loads(response)

			# return json_res
			# json_get_res = json.loads(get_res)
			return get_res
			# return jsonified_get_res

		except:
			print('hit expection')
			return Exception

edit_users_api = Blueprint('resources.edit_users', __name__)
api = Api(edit_users_api)
api.add_resource(
	EditUsers,
	'/editusers',
	endpoint='editusers'
)

