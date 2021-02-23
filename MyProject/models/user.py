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

        user = cls.query.filter_by(username=username).first()

        return user

    @classmethod
    def search_by_id(cls,id):

        user = cls.query.filter_by(id=id).first()

        return user

    def add(self):

        db.session.add(self)
        db.session.commit()