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
    else:
        print('[:] there was an error installing mysql.connector ')


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1",
  database="class" # please mention this
)

cur = db.cursor()

sql = "INSERT INTO class_mates (name, email) VALUES (%s, %s)"
val = [ # this is example of passing multile values via 1 string and 1 list, that includes tuples
  ('Amit', 'amit@somemail.com'),
  ('Victoria', 'vika@someothermail.com'),
  ('Shai', 'shai@vaiolabs.com'),
]


cur.execute(sql, val)

db.commit() # commit is needed to updating the tables

print(cur.rowcount, "record inserted.")
