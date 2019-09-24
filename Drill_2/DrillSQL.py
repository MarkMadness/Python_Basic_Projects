#
#           Drill 2 for Python Course
#
#           Mark Roenfeldt
#
#
#           write a script that creates a database and adds new data into that database.
#
#----------------------------------------------------------------------------------------------------------------------------
#           require 2 fields, an auto-increment primary integer field and a field with the data type of string.
#
#           read from the supplied list of file names at the bottom of this page and determine only the
#               files from the list which ends with a “.txt” file extension.
#
#           add those file names from the list ending with “.txt” file extension within your database.
#
#           legibly print the qualifying text files to the console.
#
#----------------------------------------------------------------------------------------------------------------------------
#           The following is the list of file names to use for this drill:
#               fileList = ('information.docx','Hello.txt','myImage.png', \
#                   'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
#

import os
import sqlite3

conn = sqlite3.connect('drill_two.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_spaceships( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_model TEXT, \
        col_year, \
        col_capacity, \
        col_textfile TEXT)")
    conn.commit()
conn.close()



fileList = ['information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']
TxtList = []
x=0
for i in fileList:
    extension = os.path.splitext(i)[-1].lower()
    if extension == ('.txt'):
        Var = os.path.join(i)
        TxtList.insert(x, Var)
        x=x+1

    

conn = sqlite3.connect('drill_two.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_spaceships(col_model, col_year, col_capacity, col_textfile) VALUES (?,?,?,?)", \
                ('Star Treker', 2374, 5000, TxtList[0]))
    cur.execute("INSERT INTO tbl_spaceships(col_model, col_year, col_capacity, col_textfile) VALUES (?,?,?,?)", \
                ('Black Hole Evader', 2756, 30, TxtList[1]))
    conn.commit()
conn.close()




conn = sqlite3.connect('drill_two.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_model, col_year, col_capacity, col_textfile FROM tbl_spaceships WHERE ID = 1")
    varShips1 = cur.fetchall()
    for item in varShips1:
        databaseprint = "   Spaceships \nModel: {}\nYear: {}\nCapacity: {}\nTxt File: {}".format(item[0],item[1],item[2],item[3])
    print(databaseprint)
    cur.execute("SELECT col_model, col_year, col_capacity, col_textfile FROM tbl_spaceships WHERE ID = 2")
    varShips2 = cur.fetchall()
    for item in varShips2:
        databaseprint = "   Spaceships \nModel: {}\nYear: {}\nCapacity: {}\nTxt File: {}".format(item[0],item[1],item[2],item[3])
    print(databaseprint)







