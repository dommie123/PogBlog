from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_data.db'
app.secret_key = 'Placeholder'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# TODO add resources below
