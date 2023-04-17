import sqlite3
from sqlite3 import Error

import doladb

ddbclient = doladb.ddb()

ddbcoll = ddbclient.get_table("test")