from flask_restful import Resource, reqparse
from MyProject.models.user import UserModel

class RegisterUser(Resource):

    myparser = reqparse.RequestParser()
    myparser.add_argument("username", required=True)
    myparser.add_argument("password", required=True)

    def post(self):

        params = RegisterUser.myparser.parse_args()
        user = UserModel.search_by_username(params["username"])
        if user:
            return "This username already exists", 400

        new_user = UserModel(**params)
        new_user.add()
        return {"message": "User registered successfully"},200