#!/usr/bin/python
import psycopg2
from config import config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

""" Connect to the PostgreSQL database server """

params = config()
print(params['database'])

con = psycopg2.connect("user=postgres password=Type2Seesaw")
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Obtain a DB Cursor

cursor = con.cursor();

name_Database = params['database']

# Create table statement

sqlCreateDatabase = "CREATE DATABASE " + name_Database + ";"

# Create a table in PostgreSQL database

cursor.execute(sqlCreateDatabase)



cursor.close()

con.close()

