from flask import Flask, g, jsonify
from flask_cors import CORS
# import models
# from resources.api import talentlms_api

import config

DEBUG = True
HOST='0.0.0.0'
PORT=8000

app = Flask(__name__)

@app.before_request
def before_request():
	print('request beginning')


@app.after_request
def after_request(response):
	print('response incoming')
	return response


@app.route('/')
def index():
	return 'hi, put the response here'

if __name__ == '__main__':
	app.run(debug=DEBUG,port=PORT)