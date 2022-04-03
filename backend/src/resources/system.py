from flask_restful import Resource

class System(Resource):
    _instance = None
    loggedUser = None

    def __init__(self):
        raise RuntimeError("Cannot call constructor on singleton instance! Use instance method instead.")

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance

    @classmethod
    def log_user(cls, user):
        cls.loggedUser = user

    @classmethod
    def logout(cls):
        cls.loggedUser = None

    def get(self):
        if self.loggedUser:
            return self.loggedUser.json(), 200
        return {'message': 'No user is currently logged in!'}, 404