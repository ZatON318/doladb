import sqlite3
from sqlite3 import Error
import json

import os

class DolaClient:
    def __init__(self,*argv):
        self.args = argv
        print("DolaDB 0.1 init")
        try:
            with open('ddb_config.json', 'r') as openfile:
                self.dola_conf = json.load(openfile)
            if("v" in self.args):
                print("Dola config found, procceding to connecting databases...")
        except FileNotFoundError:
            if("v" in self.args):
                print("No Dola config file found creating default one...")
            self.dola_conf={
                "0":{
                    "name":"dola",
                    "file_name":"dola.db",
                },
            }
            with open("ddb_config.json", "w") as conf:
                json.dump(self.dola_conf, conf)
            

    def __getitem__(self, item):
        self.new_db_id = 0
        for db in self.dola_conf:
            if item == self.dola_conf[str(db)]["name"]:
                if("v" in self.args):
                    print("DB found...")
                return database(self.dola_conf[str(db)]["name"], self.dola_conf[str(db)]["file_name"])
            self.new_db_id += 1
         
        if("v" in self.args):
            print("DB not found, creating")
        
        self.file_name = "" + item + ".db"
        self.dola_conf.update({str(self.new_db_id):{
            "name":item,
            "file_name":self.file_name
        }})
        with open("ddb_config.json", "w") as conf:
            json.dump(self.dola_conf, conf)

        return database(self.dola_conf[str(self.new_db_id)]["name"], self.dola_conf[str(self.new_db_id)]["file_name"])

        #c = self.conn.cursor()
        #query = "CREATE TABLE " + item + " (id INTEGER PRIMARY KEY);"
        #c.execute(query)

        
        #self.dola_conf

        #print("Table createt")
        #return item
        
    
    def list_database_names(self):
        self.dbs = []
        for db in self.dola_conf:
            self.dbs.append(self.dola_conf[str(db)]["name"])
        return self.dbs


class database():
    def __init__(self, *argv):
        self.name = argv[0]
        self.file_name = argv[1]
        self.conn = None
        try:
            print(self.file_name)
            self.conn = sqlite3.connect(self.file_name)
        except Error as e:
            print(e)

    def __getitem__(self, item):
        c = self.conn.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        c.execute(query)

        self.colls = c.fetchall()
        self.num_of_colls = len(self.colls)
        print(self.num_of_colls)

        for coll in self.colls:
            print(coll[0])
            if coll[0] == item:
                print("Collection found...")
                return collection(coll[0])
        
        print("Collection not found, creating...")
        query = "CREATE TABLE " + item + " (id INTEGER PRIMARY KEY);"
        c.execute(query)
        return collection(item)


    def list_collection_names(self):
        c = self.conn.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        c.execute(query)

        colls = c.fetchall()
        return colls

class collection():
    def __init__(self, *argv):
        self.name = argv[0]
    
    def __str__(self):
        return self.name
