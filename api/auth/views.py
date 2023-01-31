from flask_restx import Namespace,Resource


# create a new namespace first
# create a new resource
auth_namespace = Namespace('auth',description='a namespace for authentication')


@auth_namespace.route("/signup")
class SignUp(Resource):

    def post(self):
        """create a new user account"""
        return "created"


@auth_namespace.route("/login")
class Login(Resource):
    def post(self):
        """Login with excisting account"""
        pass

