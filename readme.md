# All Chicago TalentLMS API server

## Summary
This API is built using the Flask framework in Python.
The server can manage HTTP requests and can so far handle GET and POST requests

## MVP Use Case
* The config file (hidden) includes access to the TalentLMS database for a nonprofit organization
* Use GET requests to find users by email
* Use POST requests to edit attributes of the found user

* Currently supports assigning credit to one users at a time

## How to run
* Execute {python version} app.py to execute on a local port
* Send a proper HTTP GET request that includes the appropriate attributes in the body of a form-data object

This image explains the process internally at All Chicago and for a CoC member agency that needs to train a user


CoC credit workflow
(https://drive.google.com/file/d/1NURQHO6wXtwD2LwZ45gK1PFjxmDf_RXf/view?usp=sharing)


### Forthcoming features
* Deploy this server to cloud service so it can be reached outside of local servers
* Get core functionality without POSTMAN
* Handle POST requests to TalentLMS api/v1/edituser route
* Add instructions for creating python environment needed to execute the server
* Use templates to render a webpage capable of hitting this server's routes
* Deploy template interface