from flask import jsonify, Blueprint, abort, make_response
from flask_restful import (Resource, Api, reqparse, inputs, fields, marshal, marshal_with, url_for)

## importing these modules to handle json, responses, enable request body and body fields

user_fields = {
    ### fields to be edited
}

class User(Resource):
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

    def post(self):
        args = self.reqparse.parse_args()
        print(args,'<--- these are the arguments')
        ## any logic goes here
        # Typically, you want to send some form-encoded data — much like an HTML form. To do this, simply pass a dictionary to the data argument. Your dictionary of data will automatically be form-encoded when the request is made:
        
