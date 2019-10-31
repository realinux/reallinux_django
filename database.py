import sqlite3
import os.path

last = []
count = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "./db.sqlite3")
with sqlite3.connect(db_path) as db:

#con = sqlite3.connect("/home/reallinux/django-test/reallinux_project/splite3.db")

    cursor = db.cursor()

    cursor.execute("select * from reallinux_info")

    rows = cursor.fetchall()

    for row in rows :
        print row



        data = row[2]
        data = data.split(" ")
        date = data[0]
        date = date.split("-")
        date = " ". join(date)

        time = data[1]
        time = time.split(":")
        sec = time[2].split(".")

        #print sec
    
        time = time[0] + " " +time[1] + " " +  sec[0]


        str =  date + " " +time
        list = str.split(" ")
        
        for i in range(0,len(list)):
            list[i] = int(list[i])

        #last[count] = list
        #count = count + 1
        last.append(list)
        
        
#print last

#  [2019, 10, 8, 11, 18, 2]

month = [0] * 31

for today in last:
    day = today[2]
    month[day] = month[day] + 1


#print month





