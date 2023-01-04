
from pymongo import MongoClient

print("testing")

client = MongoClient('mongodb+srv://admin:admin@bc-database.he1iq.mongodb.net/?retryWrites=true&w=majority')
db = client['database']

collection = db.user

user = {
    "username": "test2",
    "password": '123'
}

users = db.user

post_id = users.insert_one(user).inserted_id

print(post_id)