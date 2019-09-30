#
#           Python Version 3.7.4
#
#           Author: Mark Roenfeldt
#
#
#           Write a script that creates a GUI with a button widget and a text widget. Your script will also include a function
#           that when it is called will invoke a dialog modal which will allow users with the ability to select a folder directory
#           from their system. Finally, your script will show the user’s selected directory path into the text field.
#
#           Use the askdirectory() method from the Tkinter module.
#
#           Have a function linked to the button widget so that once the button has been clicked will take the user’s selected
#           file path retained by the askdirectory() method and print it within your GUI’s text widget.

import os
import tkinter
from tkinter import *
from tkinter import filedialog

root = Tk()
ent = Entry(root)

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.minsize(800,500) #(Width,Height)
        self.master.maxsize(800,500)
        self.master.title("View files in directory")
        self.master.config(bg='lightgray')

        self.varBrowse = StringVar()
        self.varBrowse.set('')
        

        self.btnBrowse = Button(self.master,text="Check a Directory", width=15, height=2,command=self.selectdir)
        self.btnBrowse.grid(row=0,column=0, padx=(30,0), pady=(10,0))

        self.label1 = Label(self.master,text="Content: ", width=15, height=2)
        self.label1.grid(row=0,column=1, padx=(30,0), pady=(10,0))
        
        self.txtbox = Text(self.master, width=80, height=20)
        self.txtbox.grid(row=1,column=1, padx=(30,0), pady=(10,0), sticky=N+E)

        self.btnClose = Button(self.master, text="Close Program", width=15, height=3,command=self.close)
        self.btnClose.grid(row=2, column=1, padx=(270,0), pady=(10,0))

    def selectdir(self):
        #Select desired directory to check files in
        dirPath = filedialog.askdirectory()
        listPath = os.listdir(dirPath)
        #After selecting a directory show all items in the .        
        self.txtbox.insert(INSERT, listPath)
        

    def close(self):
        #Close the ParentWindow
        self.master.destroy()






if __name__ == "__main__":
    App = ParentWindow(root)
    root.mainloop()


'''
        top = self.top=Toplevel()
        text=Text(root,height=10,width=50)
        self.e=text(top)
        self.e.pack(padx=5)
        b=Button(top,text="OK",command=self.ok)
        b.pack(pady=5)
        print("Diretory Path: " + dirPath)
        def ok(self):
            print('\nFiles in Directory: ' + listPath)
            self.top.destroy()

'''
