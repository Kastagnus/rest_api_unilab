import sqlite3
from MyProject.resources import hotel_rooms
from MyProject.security import users

# connection = sqlite3.connect("hotelrooms.db")
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS hotel_rooms(id INTEGER PRIMARY KEY, room_type text, price int , quantity int)")
# query_string = "INSERT INTO hotel_rooms VALUES(?,?,?,?)"
# for room in hotel_rooms:
#     params = room.id, room.room_type, room.price, room.quantity
#     cursor.execute(query_string,params)
# connection.commit()
# connection.close()

# connection = sqlite3.connect("userlist.db")
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS user_table(id INTEGER PRIMARY KEY, username text, password text)")
# query_string = "INSERT INTO user_table VALUES(?,?,?)"
# for user in users:
#     params = user.id, user.username, user.password
#     cursor.execute(query_string,params)
# connection.commit()
# connection.close()

# connection = sqlite3.connect("userlist.db")
# cursor = connection.cursor()
# query = "DROP TABLE user_table"
# cursor.execute(query, ())
# connection.commit()
# connection.close()