from flask import jsonify, Blueprint, abort, make_response
from flask_restful import (Resource, Api, reqparse, inputs, fields, marshal, marshal_with, url_for)

## importing these modules to handle json, responses, enable request body and body fields

user_fields = {
    ### fields to be edited
}

class Users(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            ## 'arguments' as str objs,
        required=True,
        help='demonstration',
        location=['form','json']  
    )
        ## use this syntax to add further arguments for the req parser

    ## call constructor methods
    super().__init__()

    	def get(self):
		try: 
			print('calling user route to get users')

			lms_header = {'user':config.api_key,'password':'','setApiKey':config.api_key,'setDomain':config.home_domain,'content-type':'application/json'}
			headers = lms_header
			print(headers, '<-- HTTP Basic headers')
			payload = {'username':'mrobinson'}
			req = requests.get('https://allchicago.talentlms.com/api/v1/users/username:',params=payload, headers=headers, auth=HTTPBasicAuth(config.api_key,''))
			# /v1/users/username:{userName} 
			res = req.text
			status = req.status_code
			print('request successful')
			json_loaded_res = json.loads(res)
			# ## load response as json
			# changessss
			return json_loaded_res, status
		except:
			print('hit exception')
			return Exception

    def post(self):
        args = self.reqparse.parse_args()
        print(args,'<--- these are the arguments')
        ## any logic goes here
        # Typically, you want to send some form-encoded data — much like an HTML form. To do this, simply pass a dictionary to the data argument. Your dictionary of data will automatically be form-encoded when the request is made:
        
users_api = Blueprint('resources.user',__name__)
api = Api(users_api)
api.add_resource(
    Users,
    '/users',
    endpoint='users'
)