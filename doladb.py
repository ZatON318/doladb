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
                "dola":{
                    "name":"dola",
                    "file_name":"dola.json",
                },
            }
            with open("ddb_config.json", "w") as conf:
                json.dump(self.dola_conf, conf, indent=1)
            

    def __getitem__(self, item):
        try:
            db = self.dola_conf[item]
            print("db found")
        except:
            print("no db found")
            self.file_name = "" + item + ".json"
            self.dola_conf.update({str(item):{
                "name":item,
                "file_name":self.file_name
            }})
            with open("ddb_config.json", "w") as conf:
                json.dump(self.dola_conf, conf, indent=1)

            #self.db = {}
            #with open(item + ".json", "w") as db:
            #    json.dump(self.db, db, indent=1)

            
        return database(self.dola_conf[item]["name"], self.dola_conf[item]["file_name"])
    
    def list_database_names(self):
        self.dbs = []
        for db in self.dola_conf:
            self.dbs.append(self.dola_conf[str(db)]["name"])
        return self.dbs


class database():
    def __init__(self, *argv):
        self.name = argv[0]
        self.file_name = argv[1]
        self.args = argv
        try:
            with open(self.file_name, 'r') as openfile:
                self.db = json.load(openfile)
            if("v" in self.args):
                print("DB found...")
        except FileNotFoundError:
            if("v" in self.args):
                print("DB not foun, creating...")
            self.db={
                self.name:{
                    "name":self.name,
                    "file_name":self.file_name,
                    "collections":{},
                },
            }
            with open(self.file_name, "w") as conf:
                json.dump(self.db, conf, indent=1)

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
                return collection(coll[0], self)
        
        print("Collection not found, creating...")
        query = "CREATE TABLE " + item + " (id INTEGER PRIMARY KEY);"
        c.execute(query)
        return collection(item, self)


    def list_collection_names(self):
        return self.db[self.name]["collections"]

class collection():
    def __init__(self, *argv):
        self.name = argv[0]
        self.db = argv[1]
    
    def __str__(self):
        return self.name

    def insert_one(self, db):
        c = self.db.conn.cursor()
        query = f"INSERT INTO {self.name}(t1) VALUES (?);"
        c.execute(query, ["test"])
        self.db.conn.commit()
        print(self.db)
