import sqlite3
from flask import Flask
from flask_restful import Resource,Api, reqparse
from MyProject.models.user import UserModel

class RegisterUser(Resource):

    myparser = reqparse.RequestParser()
    myparser.add_argument("username", required=True)
    myparser.add_argument("password", required=True)

    def post(self):

        params = RegisterUser.myparser.parse_args()
        new_user = UserModel(**params)
        new_user.add()
        return {"message":"User registered successfully"}