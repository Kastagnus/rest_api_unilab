from db import db

class HotelRooms(db.Model):

    __tablename__ = "hotel_rooms"

    id = db.Column(db.Integer, primary_key=True)
    room_type = db.Column(db.String)#(characte count)
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __init__(self,room_type, price, quantity):

        self.room_type = room_type
        self.price = price
        self.quantity = quantity

    def json(self):
        return {"room_type":self.room_type,"price":self.price,"quantity":self.quantity}

    @classmethod
    def findbyname(cls, room_type):
        room = cls.query.filter_by(room_type=room_type).first()
        return room


    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()