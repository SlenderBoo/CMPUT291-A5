import pymongo

#connect to mongodb
client = pymongo.MongoClient(
    "mongodb://yuxin19:chen991008@cluster0-shard-00-00.r1efp.mongodb.net:27017,cluster0-shard-00-01.r1efp.mongodb.net:27017,cluster0-shard-00-02.r1efp.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-tb89xj-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client['A5db']
col = db.listings

cursor = col.aggregate([
    {"$group": {"_id": {"host_id": "$host_id"}, "count":{"$sum": 1}}},
    # sort all the docs by host_id
    {"$sort": {"_id": 1}},
    #Take the first 10 row
    {"$limit": 10},
])

#print out the result
result = list(cursor)
for i in result:
    print(i)
