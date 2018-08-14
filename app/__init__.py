import sys

import yaml

from flask import Flask
from flask_cors import CORS

from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

try:
    global_config = yaml.load(open("configuration/config.yml"))

    host = str(global_config['SERVER']['host'])  # Server Host
    port = int(global_config['SERVER']['port'])  # Server Port

    db = MongoClient(connect=False)
    db = db[global_config['DATABASE']['db']]
    user = db[global_config['DATABASE']['collection1']]
    posts = db[global_config['DATABASE']['collection2']]

    consumer_key = global_config['TWITTER']['consumer_key']
    consumer_secret = global_config['TWITTER']['consumer_secret']
    api_key = global_config['TWITTER']['api_key']
    api_secret = global_config['TWITTER']['api_secret']

    from app.api.v1.routes import *


except Exception as e:
    app.logger.info("Error occurred while parsing configurations and blueprint registration.")
    app.logger.exception(e)
    sys.exit(1)
