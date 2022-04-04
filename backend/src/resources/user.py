from winreg import REG_RESOURCE_LIST
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import hashlib

from models.user_model import User

class RUser(Resource):
    # @jwt_required
    def get(self, user_id):
        user = User.find_by_id(user_id)
        if user:
            return user.json(), 200
        return {'message': 'This user does not exist within the database!'}, 404

    # @jwt_required
    def delete(self, user_id):
        user = User.find_by_id(user_id)
        if user:
            user.delete_from_db()
        return {'message': 'Success!'}, 410


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type=str,
        required=True,
        help="A user must have a username!",
    )
    parser.add_argument('first_name', 
        type=str,
        required=True,
        help="A user must have a first name!",
    )
    parser.add_argument('last_name', 
        type=str,
        required=True,
        help="A user must have a last name!",
    )
    parser.add_argument('email', 
        type=str,
        required=True,
        help="A user must have a valid email address!",
    )
    parser.add_argument('password', 
        type=str,
        required=True,
        help="A user must have a password so they can be safe!",
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        user = User.find_by_username(data['username'])
        if user:
            return {'message': 'This user already exists within the database!'}, 409
        user = User(**data)
        try:
            user.save_user()
        except Exception as ex:
            return {'message': f'An error occurred while saving this user! \nError: {ex}'}, 500
        return user.json(), 201

    # This exists to allow users to change their settings
    def put(self):
        data = UserRegister.parser.parse_args()
        user = User(data['username'], **data)
        status_code = 202
        if not user:
            user = User(**data)
            status_code = 201
        else:
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']

            new_password = hashlib.sha256(data['password'].encode('utf-8')).hexdigest()
            user.password = new_password

            status_code = 200
        
        user.save_user()    
        return user.json(), status_code