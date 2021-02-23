from flask import Flask, redirect
from flask_restful import Api
from flask_jwt import JWT
from MyProject.security import authentication, identity
from MyProject.resources.hotel_rooms import All_Room, Room
from MyProject.resources.user import RegisterUser

app = Flask(__name__)
app.secret_key = "New_Secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///alldata.db"
app.config['PROPAGATE_EXCEPTIONS'] = True
appI = Api(app)
jwt = JWT(app, authentication, identity)


@app.route("/")
def home():

    return redirect("https://github.com/Kastagnus/rest_api_unilab/tree/main"), 302

appI.add_resource(All_Room, "/about/")
appI.add_resource(Room, "/about/<string:room_type>")
appI.add_resource(RegisterUser, "/registration/")
