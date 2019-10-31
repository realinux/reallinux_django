import sqlite3
import os.path

last = []
count = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "./db.sqlite3")
with sqlite3.connect(db_path) as db: 

    cursor = db.cursor()

    cursor.execute("select * from reallinux_info")

    rows = cursor.fetchall()

    for row in rows :
        print row 
