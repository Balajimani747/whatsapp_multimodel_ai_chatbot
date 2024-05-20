from flask_pymongo import PyMongo
from pymongo import MongoClient
from application import MONGO_URI


client = MongoClient(MONGO_URI)
db = client['food_nest']
users_table = db['users']                  #User
restaurent_table = db['restaurants']       #Restaurent