from flask import jsonify

from flask_restful import (Resource, Api, reqparse, url_for)

import requests

## both of these classes are inherited from the Resource
## because we're importing from flask_restful, classes are given resource, resource enables the classes to handle all HTTP request and response methods

## Setting up View Functions

## Setting up third party api requests

r_get = requests.get()

r_get('https://api.github.com/events'):
	print(r.content)
	