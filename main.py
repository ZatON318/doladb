import doladb

myclient = doladb.DolaClient("v")

mydb = myclient["testdb"]
print(mydb)
print(mydb.list_collection_names())
#mycol = mydb["customers"]

#mydict = { "name": "John", "address": "Highway 37" }

#x = mycol.insert_one(mydict)
#print(x.inserted_id) 