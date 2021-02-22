import sqlite3
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from MyProject.models.hotelrooms import HotelRooms


class All_Room(Resource):

    def get(self):
        connection = sqlite3.connect("hotelrooms.db")
        cursor = connection.cursor()
        query = "SELECT * FROM hotel_rooms"
        result = cursor.execute(query, ())
        rooms = result.fetchall()
        connection.commit()
        connection.close()
        return rooms, 200

    @jwt_required()
    def delete(self):
        connection = sqlite3.connect("hotelrooms.db")
        cursor = connection.cursor()
        query = "DELETE FROM hotel_rooms"
        cursor.execute(query, ())
        return "All the rooms deleted successfully!", 200

class Room(Resource):
    my_parser = reqparse.RequestParser()
    my_parser.add_argument("room_type", type=str, required=True)
    my_parser.add_argument("price", type=float, required=True)
    my_parser.add_argument("quantity", type=int, required=True)

    def get(self, room_type):

        room = HotelRooms.findbyname(room_type)
        if room:
            return room.json()

        return {"message":"This room doesn't exist"}

    def post(self, room_type):
        room = HotelRooms.findbyname(room_type)
        if room:
            return "This room already exists", 400

        params = Room.my_parser.parse_args()
        new_room = HotelRooms(params["room_type"], params["price"], params["quantity"])
        new_room.save_to_db()
        return "New room has been added successfully", 200

    def put(self, room_type):
        room = HotelRooms.findbyname(room_type)
        params = Room.my_parser.parse_args()

        if room:

            room.price = params["price"]
            room.quantity = params["quantity"]

        room = HotelRooms(*params)

        room.save_to_db()

        return "Successful operation", 200


    def delete(self, room_type):

        room = HotelRooms.findbyname(room_type)
        if room:
            room.delete_from_db()
            return "Item deleted successfully", 200

        return "This item doesn't exist", 400