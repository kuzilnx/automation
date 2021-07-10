#!/usr/bin/env python3

import os,sys
import subprocess
import time
try:
    import mysql.connector
except:
    print("[!] missing mysql connector")
    time.sleep(2)
    print("[+] trying to fix the library dependancy")
    time.sleep(2)
    os_out = subprocess.call('pip3 install mysql.connector',shell=True)
    if os_out.returncode == 0:
        print('[:] mysql.connector installed successfully, try to re-run script')
        sys.exit(0)
    else:
        print('[:] there was an error installing mysql.connector ')
        sys.exit(1)

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1",
  database="class" # please mention this
)

cur = db.cursor()

sql = "INSERT INTO class_mates (name, email) VALUES (%s, %s)" # only 2 values are passed, because first column is auto increment and no need to change it
val = ("Alex M. Schapelle", "alex@vaiolabs.com")
cur.execute(sql, val) # we are passing 2 strings can be passed to sql to specific columns

db.commit() # commit is needed to updated the tables

print(cur.rowcount, "record inserted.")
