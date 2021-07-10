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

cur.execute("CREATE TABLE class_mates (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")
                                            #this is how primary key is set
