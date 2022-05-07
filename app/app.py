
from __future__ import absolute_import

import os

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

config = {
    "development": "app.configs.DevelopmentConfig",
    "testing": "app.configs.TestingConfig",
    "production": "app.configs.ProductionConfig"
}

app.config.from_object(config[os.getenv('FLASK_CONFIGURATION', 'development')])

#
# @app.route('/')
# def notmain():
#     return {'welcome to greatjobs':'wait for updates please'}


# from views.core_services import *
