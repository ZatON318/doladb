import sqlite3
from sqlite3 import Error

import doladb

myclient = doladb.DolaClient("v")

mydb = myclient["test"]

#print(mydb)
#print(myclient.list_database_names())

mycoll = mydb["table1"]

print("collection: " + str(mycoll))

#mydb.list_collection_names()