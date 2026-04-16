from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db_mongo = client["MyAuth"]
collection = db_mongo["users"]