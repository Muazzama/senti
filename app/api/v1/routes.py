import json
from app import app
from flask import Response

@app.route('/', methods=['GET', 'POST'])
def index():

    data = {
        'message': 'Welcome to SentiWorld'
    }

    response = Response(json.dumps(data), status=200, mimetype='application/json')
    return response

@app.route('/login', methods=['GET', 'POST'])
def index():

    data = {
        'message': 'Welcome to SentiWorld Login'
    }

    response = Response(json.dumps(data), status=200, mimetype='application/json')
    return response

@app.route('/logout', methods=['GET', 'POST'])
def index():

    data = {
        'message': 'Welcome to SentiWorld Logout'
    }

    response = Response(json.dumps(data), status=200, mimetype='application/json')
    return response

@app.route('/register', methods=['GET', 'POST'])
def index():

    data = {
        'message': 'Welcome to SentiWorld Registration'
    }

    response = Response(json.dumps(data), status=200, mimetype='application/json')
    return response

@app.route('/home', methods=['GET', 'POST'])
def index():

    data = {
        'message': 'Welcome to SentiWorld Input Page'
    }

    response = Response(json.dumps(data), status=200, mimetype='application/json')
    return response

@app.route('/dashboard', methods=['GET', 'POST'])
def index():

    data = {
        'message': 'Welcome to SentiWorld Dashboard'
    }

    response = Response(json.dumps(data), status=200, mimetype='application/json')
    return response




