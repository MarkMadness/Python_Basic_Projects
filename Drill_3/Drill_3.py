#
#           Python Version 3.7.4
#
#           Author: Mark Roenfeldt
#
#           Create an exact copy of the GUI in Drill 3 on Step 121 of the Python Course

import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.minsize(600,180) #(Width,Height)
        self.master.maxsize(600,180)
        self.master.title("Check files")
        self.master.config(bg='lightgray')

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()
        self.varBrowse1.set('')
        self.varBrowse2.set('')

        self.btnBrowse1 = Button(self.master,text="Browse...", width=15, height=2)
        self.btnBrowse1.grid(row=0,column=0, padx=(30,0), pady=(10,0))
        
        self.btnBrowse2 = Button(self.master,text="Browse...", width=15, height=2)
        self.btnBrowse2.grid(row=1,column=0, padx=(30,0), pady=(10,0))

        self.txtboxfirst = Entry(self.master,text=self.varBrowse1, width=40)
        self.txtboxfirst.grid(row=0, column=1, padx=(30,0), pady=(10,0), sticky=N+E)

        self.txtboxsecond = Entry(self.master,text=self.varBrowse2, width=40)
        self.txtboxsecond.grid(row=1,column=1, padx=(30,0), pady=(10,0), sticky=N+E)

        self.btnRun = Button(self.master, text="Check for files...", width=15, height=3)
        self.btnRun.grid(row=2, column=0, padx=(30,0), pady=(10,0))

        self.btnClose = Button(self.master, text="Close Program", width=15, height=3)
        self.btnClose.grid(row=2, column=1, padx=(270,0), pady=(10,0))
        






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
