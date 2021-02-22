from MyProject.db import db

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

    @classmethod
    def all_data(cls):

        return {"rooms":list(map(lambda room: room.json(), cls.query.all()))}

    def json(self):
        return {"room_type":self.room_type,"price":self.price,"quantity":self.quantity}

    @classmethod
    def find_by_name(cls, room_type):
        room = cls.query.filter_by(room_type=room_type)
        return room


    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()