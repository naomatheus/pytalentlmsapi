from flask import jsonify, Blueprint, abort, make_response, request
from flask_restful import (Resource, Api, reqparse, inputs, fields, marshal, marshal_with, url_for)
import json
import config 
import requests 
from requests.auth import HTTPBasicAuth

## importing these modules to handle json, responses, enable request body and body fields

user_fields = {
    ### fields to be edited
}

class Users(Resource, requests.auth.AuthBase):
    # def __call__(self,r):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='No username provided',
            location=['form', 'json']
    )

       
    ## call constructor methods
        super().__init__()

    def get(self):
        try:
            print('calling user route')

            print(requests, '<-- requests object')

            lms_header = {'user':config.api_key,'password':'','setApiKey':config.api_key,'setDomain':config.home_domain,'content-type':'application/x-www-form-urlencoded'}

            headers = lms_header
            print(headers,'<-- http basic headers')
            

            req = requests.get('https://allchicago.talentlms.com/api/v1/users/username:', headers=headers, auth=HTTPBasicAuth(config.api_key,''))

            print(req.content, '<-- content')

            res = req.text
            status = req.status_code
            print('request successful')
            json_loaded_res = json.loads(res)

            print()
            return json_loaded_res, status
        except:
            print('hit exception')
            return Exception

    # def post(self):
        
    #     try:
    #         args = self.reqparse.parse_args()
    #         print(args,'<-- these are args')

    #         lms_header = {'user':config.api_key,'password':'','setApiKey':config.api_key,'setDomain':config.home_domain,'content-type':'application/x-www-form-urlencoded'}

    #         headers = lms_header

    #         req = requests.post('https://allchicago.talentlms.com/api/v1/users/username:', headers=headers, auth=HTTPBasicAuth(config.api_key,''),data=args)

    #         print(req.content, '<-- content')

    #         res = req.text
    #         status = req.status_code
    #         print('request successful')
    #         json_loaded_res = json.loads(res)

            
    #         return json_loaded_res, status
    #         ## any logic goes here
    #     # Typically, you want to send some form-encoded data — much like an HTML form. To do this, simply pass a dictionary to the data argument. Your dictionary of data will automatically be form-encoded when the request is made:

    #     except:
    #         return Exception
        
    def post(self):
        try:
            args = self.reqparse.parse_args()
            print(args,'<-- args in put route')

            lms_header = {'user':config.api_key,'password':'','setApiKey':config.api_key,'setDomain':config.home_domain,'content-type':'application/x-www-form-urlencoded'}

            headers = lms_header

            edit_req = requests.post('https://allchicago.talentlms.com/api/v1/edituser', headers=headers, auth=HTTPBasicAuth(config.api_key,''),data=args)

            edit_res = edit_req.text
            status = edit_req.status_code

            print(edit_res, '<-- edit res')

            # print(json_loaded_edit_res,'<-- json patched res')


            return edit_res
        except:
            return Exception
        



        
users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(
    Users,
    '/users',
    endpoint='users'
)