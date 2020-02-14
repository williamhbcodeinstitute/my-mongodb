import pymongo
import os
from os import path
if path.exists("env.py"):
    import env


MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "MyFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

new_docs = [{'first': 'terry', 'last': 'pratchett', 'gender': 'm', 'dob': '28/04/1948', 'hair_colour': 'brown', 'occupation': 'writer', 'nationality': 'english'},
{'first': 'george', 'last': 'may', 'gender': 'm', 'dob': '11/09/1991', 'hair_colour': 'brown', 'occupation': 'Home', 'nationality': 'english'}]
coll.insert_many(new_docs)

documents = coll.find()

for doc in documents:
    print(doc)