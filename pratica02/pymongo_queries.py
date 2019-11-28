from pymongo import *

cli = MongoClient()
rest = cli["cbd"]["rest"]

def count_local():
    return rest.aggregate([{"$group": {"_id": "$localidade"}}, {"$count": "Number of Restaurants"}])

def count_by_local():
    return rest.aggregate([{"$group": {"_id": "$localidade", "num": {"$sum": 1}}}])

def count_by_gastro_local():
    return rest.aggregate([{"$group": {"_id": {"local": "$localidade", "gastro":"$gastronomia" }, "num":{"$sum":1}}}])

def rest_with_name(name):
    return rest.find({"nome": {"$regex":name}})

count=0
for l in rest_with_name("Park"):
    print(l)
    count+=1
    if count>5:
    	break

