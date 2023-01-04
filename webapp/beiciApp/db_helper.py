
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

client = MongoClient('mongodb+srv://admin:admin@bc-database.he1iq.mongodb.net/?retryWrites=true&w=majority')
db = client['database']


def insert_one(collection, doc):
    id = db[collection].insert_one(doc).inserted_id
    return id 

