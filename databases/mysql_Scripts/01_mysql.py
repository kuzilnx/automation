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
  password="1" # if you have not run mysql_secure_connection password is not needed
)

cur = db.cursor()

cur.execute("CREATE DATABASE class")
# execute is the function to communicating with sql commads


cur.execute("SHOW DATABASES")

for database in cur:
  print(database)
