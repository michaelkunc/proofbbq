# TODO this is where prod configuration will live
from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)

# DB
db = client.proof

# Collections
cook = db.cook
