#           
#           Python Course: Drill 5, Step 123
#           
#           Mark Roenfeldt
#
#============================================================================================================================          
#           Your new script will need to provide the user with a graphical user interface that includes two buttons allowing
#           the user to browse their own system and select a source directory and a destination directory. Your script should
#           also show those selected directory paths in their own corresponding text fields.
#
#           Next, your script will need to provide a button for the user to execute a function that should iterate through
#           the source directory, checking for the existence of any files that end with a “.txt” file extension and if so,
#           cut the qualifying files and paste them within the selected destination directory.
#
#           Finally, your script will need to record the file names that were moved and their corresponding modified
#           time-stamps into a database and print out those text files and their modified time-stamps to the console.
#
#============================================================================================================================
#           use the listdir() method from the OS module to iterate through all files within a specific directory.
#           
#           use the path.join() method from the OS module to concatenate the file name to its file path, forming an absolute
#           path.
#
#           use the getmtime() method from the OS module to find out the latest date the file has been created or last
#           modified.
#
#           create a database to record the qualifying file and corresponding modified time-stamp.
#
#           print each file ending with a “.txt” file extension and its corresponding mtime to the console.
#
#           use the move() method from the Shutil module to cut all qualifying files and paste them within the destination
#           directory.
#
#============================================================================================================================
#
#           use the directory you had previously created on your system from an earlier drill assignment.
#
#           have at least 10 different files types, two of which should be text documents that end with the “.txt” file
#           extension.


import os
import sqlite3
import shutil
import time
import tkinter
from tkinter import *
from tkinter import filedialog

conn = sqlite3.connect('drill5.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists tbl_transfer(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT, \
        col_date_modified)")
    conn.commit()
conn.close()

TxtList = []
x=0

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)

        self.master = master
        self.master.minsize(1100,300)
        self.master.maxsize(1100,300)
        self.master.title("Drill 5. Cut and Paste .txt to directory")
        self.master.config(bg='lightgray')

        self.lblheader = Label(self.master,text="Select two directories you wish to move .txt files to and from",width=50,bg='lightgray')
        self.lblheader.grid(row=0,column=0,columnspan=2)

        self.btnsource = Button(self.master,text='Source',width=15,height=2,command=self.selectsource)
        self.btnsource.grid(row=1,column=0,sticky=N+W)
        self.txtsource = Text(self.master,width=100,height=2)
        self.txtsource.grid(row=1,column=1,padx=5,pady=5)

        self.btndestin = Button(self.master,text='Destination',width=15,height=2,command=self.selectdestin)
        self.btndestin.grid(row=2,column=0,sticky=N+W)
        self.txtdestin = Text(self.master,width=100,height=2)
        self.txtdestin.grid(row=2,column=1,padx=5,pady=5)

        self.btnCutPaste = Button(self.master,text="Cut and Paste .txt files",width=25,height=2,command=self.operation)
        self.btnCutPaste.grid(row=3,column=1,padx=5,pady=5)

        
        self.btnClose = Button(self.master,text="Close Program",width=15,height=2,command=self.close)
        self.btnClose.grid(row=4,column=2,padx=20,pady=10)


#=====Functions=====
    def selectsource(self):
        self.sourcePath = filedialog.askdirectory()        
        self.txtsource.insert(INSERT, self.sourcePath)

    def selectdestin(self):
        self.destinPath = filedialog.askdirectory()
        self.txtdestin.insert(INSERT, self.destinPath)

    def operation(self):
        dirSource = os.listdir(self.sourcePath)
        for file in dirSource:
            if file.endswith('.txt'):
                joinPath = os.path.join(self.sourcePath, file)
                modTime = os.path.getmtime(joinPath)
                localTime = time.ctime(modTime)
                shutil.move(joinPath, self.destinPath)
                print('A .txt file transfered": ' + file)
                #Add info into database
                conn=sqlite3.connect('drill5.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO tbl_transfer(col_filename, col_date_modified) VALUES (?,?)", (file, localTime))
                print("     Modified: ", localTime)

    def close(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
