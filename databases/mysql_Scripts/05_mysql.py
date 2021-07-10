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

cur.execute("SELECT * FROM class_mates")

query = cur.fetchall() #We use the fetchall() method, which fetches all rows from the last executed statement
                       # If you are only interested in one row, you can use the fetchone() method.


for q in query:
    print(q)
