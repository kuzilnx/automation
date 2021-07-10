#!/usr/bin/env python3

import sqlite3


# connection object to db
con = sqlite3.connect('/tmp/mydatabase.db')

## function to create and insert values to db
def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    
    # commit function send/writes data to db !!!! Must Have !!!!
    con.commit()

ent = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')

# calling the function
sql_insert(con, ent)
