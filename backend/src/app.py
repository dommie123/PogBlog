from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.user import RUser, UserRegister
from resources.post import RPost, PostList
from resources.system import System

from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_data.db'
app.secret_key = 'Placeholder'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(RUser, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(RPost, '/post/<string:title>')
api.add_resource(PostList, '/posts')
api.add_resource(System, '/sys')
