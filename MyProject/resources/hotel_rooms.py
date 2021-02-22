from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from MyProject.models.hotelrooms import HotelRooms


class All_Room(Resource):

    @jwt_required()
    def get(self):
        try:
            allroom = HotelRooms.retrieve_all_data()
        except:
            return {"message":"no access"}, 404
        else:
            return allroom, 200

    def delete(self):
        # connection = sqlite3.connect("alldata.db")
        # cursor = connection.cursor()
        # query = "DELETE FROM hotel_rooms"
        # cursor.execute(query, ())
        # allroom = HotelRooms.retrieve_all_data()
        # for room in allroom["rooms"]:
        #     room.delete_from_db()
        HotelRooms.delete_all_data()
        return "All the rooms deleted successfully!", 200

class Room(Resource):
    my_parser = reqparse.RequestParser()
    my_parser.add_argument("room_type", type=str, required=True)
    my_parser.add_argument("price", type=int, required=True)
    my_parser.add_argument("quantity", type=int, required=True)

    @jwt_required()
    def get(self, room_type):

        room = HotelRooms.find_by_name(room_type)
        if room:
            return room.json()

        return {"message":"This room doesn't exist"}

    def post(self, room_type):
        room = HotelRooms.find_by_name(room_type)
        if room:
            return "This room already exists", 400

        params = Room.my_parser.parse_args()
        new_room = HotelRooms(**params)
        new_room.save_to_db()
        return "New room has been added successfully", 200

    def put(self, room_type):
        room = HotelRooms.find_by_name(room_type)
        params = Room.my_parser.parse_args()

        if room:

            room.price = params["price"]
            room.quantity = params["quantity"]

        room = HotelRooms(**params)

        room.save_to_db()

        return "Successful operation", 200


    def delete(self, room_type):

        room = HotelRooms.find_by_name(room_type)
        if room:
            room.delete_from_db()
            return "Item deleted successfully", 200

        return "This item doesn't exist", 400