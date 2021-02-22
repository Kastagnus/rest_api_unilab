import sqlite3
from MyProject.db import db

class UserModel(db.Model):

    __tablename__ = "user_table"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(8))
    def __init__(self,username,password):

        self.username = username
        self.password = password

    @classmethod
    def search_by_username(cls,username):
        # connection = sqlite3.connect("userlist.db")
        # cursor = connection.cursor()
        # query = "SELECT * FROM user_table WHERE username=?"
        # result = cursor.execute(query,(username,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        user = cls.query.filter_by(username=username).first()

        return user

    @classmethod
    def search_by_id(cls,id):
        # connection = sqlite3.connect("userlist.db")
        # cursor = connection.cursor()
        # query = "SELECT * FROM user_table WHERE id=?"
        # result = cursor.execute(query,(id,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        user = cls.query.filter_by(id=id).first()

        return user

    def add(self):
        # username = cls.search_by_username(params.get("username"))
        # if username is not None:
        #     return "Sorry this account already exists", 400
        #
        # connection = sqlite3.connect("userlist.db")
        # cursor = connection.cursor()
        # query = "INSERT INTO main.user_table VALUES(NULL,?,?)"
        # cursor.execute(query,(*params.values(),))
        # connection.commit()
        # connection.close()
        db.session.add(self)
        db.session.commit()