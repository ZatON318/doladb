import sqlite3
from sqlite3 import Error

import os

class ddb:
    def __init__(self):
        print("DolaDB 0.1 init...")
        try:
            self.conn = sqlite3.connect(r"dola.db")
        except Error as e:
            print(e)
    
    def get_table(self, name):
        c = self.conn.cursor()
        c.execute(''' SELECT count(name) FROM sqlite_sequence WHERE name='test' ''')
        result = c.fetchone()[0]
        if result==1:
            print('Table exists.')
        return(result)

    

