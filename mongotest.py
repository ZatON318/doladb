import pymongo

myclient = pymongo.MongoClient("mongodb+srv://@cluster0.7lmq6xj.mongodb.net/?retryWrites=true&w=majority")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
print(x.inserted_id) 
