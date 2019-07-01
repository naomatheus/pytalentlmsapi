from flask import jsonify, Blueprint, abort, make_response, request
from flask_restful import (Resource, Api, reqparse, inputs, fields, marshal, marshal_with, url_for)
import json
import config
import requests
from requests.auth import HTTPBasicAuth

class EditUsers(Resource, requests.auth.AuthBase):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument(
			'username',
			required=True,
			help='no username provided',
			location=['form','json']
		)

		super().__init__()

	def post(self):
		try:
			print('calling edit users route')

			lms_header = {'user':config.api_key,'password':'','setApiKey':config.api_key, 'setDomain':config.home_domain, 'content-type':'application/x-www-form-urlencoded'}

			headers = lms_header

			args = self.reqparse.parse_args()
			# dict_args = dict.items(args)
			print(args,'<-- args as dict')
			get_req = requests.post(f'https://allchicago.talentlms.com/api/v1/users/username:', headers=headers, auth=HTTPBasicAuth(config.api_key,''),data=args)

			get_res = get_req.text
			print(get_res,'<-- the get response')
			## This initial call will get/select the user to be edited

			payload = {"username":"MRobinson", "credits":"25"}
			req = requests.post(f'https://allchicago.talentlms.com/api/v1/edituser', headers=headers, auth=HTTPBasicAuth(config.api_key,''),data=payload)

			res = req.text
			status = req.status_code
			print('request successful')
			print(req.text,'<-- edituser api call req.text')

			json_res = json.loads(res)

			return json_res

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

