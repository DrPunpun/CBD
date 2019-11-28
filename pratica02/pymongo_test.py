from pymongo import *
import datetime

mongo_cli = MongoClient()

db = mongo_cli['cbd']
col = db['pymongo']

def insert_data(data):
    return col.insert(data)

def search(data):
    return col.find(data)

def edit(query, data):
    return col.update_one(query, {"$set": data})

post =  {"author": "Mike", \
        "text": "My first blog post!",\
        "tags": ["mongodb", "python", "pymongo"],\
        "date": datetime.datetime.utcnow()}

post_in = insert_data(post)
for p in search({}):
    print(p)
for p in search({"author":"Mike"}):
    print(p)

edit({"author":"Mike"}, {"author":"Steve"})
for p in search({"author":"Steve"}):
    print(p)

mongo_cli.close()