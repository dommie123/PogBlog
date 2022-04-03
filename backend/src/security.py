from re import I
from models.user_model import User
import hashlib

def authenticate(username, password):
    user = User.find_by_username(username)
    pass_attempt = hashlib.sha256(password).hexdigest()
    if user and pass_attempt == user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)