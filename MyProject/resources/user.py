import sqlite3
from flask import Flask
from flask_restful import Resource,Api, reqparse
from models.user import UserModel

class RegisterUser(Resource):

    myparser = reqparse.RequestParser()
    myparser.add_argument("username", required=True)
    myparser.add_argument("password", required=True)

    def post(self):

        params = RegisterUser.myparser.parse_args()
        return UserModel.add(params)