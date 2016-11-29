# Python Version 3.6
#
# Author: Tanvir Khondakar
#
# Purpose: Python application using Tkinter, which transfers files from one folder to another and
# saves last file transfer procedure


#============================================================================================

# Import Tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Import os
import os

# Import other modules
import time
import datetime
from datetime import timedelta
import shutil
import sqlite3

# Import related files
import move_main
import move_gui


#============================================================================================

# Create Database and running it for the first time:

def create_db(self):
    conn = sqlite3.connect('move.db')
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS move_table(unix REAL, datestamp TEXT)")
    conn.commit()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('move.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            unix = int(time.time())
            date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
            cur.execute("""INSERT INTO move_table(unix,datestamp) VALUES (?,?)""",(unix, date))
            conn.commit()
    conn.close()
    
def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM move_table""")
    count = cur.fetchone()[0]
    return cur, count

# ============================================================================================

# Functions:

# Catch if the user clicks on the windows upper-right 'X', to ensure that they want to close

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes the app
        self.master.destroy()
        os._exit(0)

def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('move.db')
    with conn:
        c = conn.cursor()
        c.execute(""" SELECT COUNT(*) FROM move_table""")
        count = c.fetchone()[0]
        i = 0
        while i < count:
            c.execute(""" SELECT datestamp FROM move_table""")
            varList = c.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()

def org_select(self):
    self.org_select = filedialog.askdirectory()
    if self.org_select is not None:
            self.labl = tk.Label(self.master, text="{}".format(self.org_select), bg = "yellow")
            self.labl.grid(row = 1, column = 0, padx =(20,10), pady = (5,0))
    else:
            messagebox.showinfo('Update','Select Transfer Folder')
    return self.org_select
            
def dst_select(self):
    self.dst_select = filedialog.askdirectory()
    if self.dst_select is not None:
            self.labl = tk.Label(self.master, text="{}".format(self.dst_select), bg = "yellow")
            self.labl.grid(row = 4, column = 0, padx =(20,10), pady = (5,0))
    else:
            messagebox.showinfo('Update','Select Transfer Folder')
    return self.dst_select

def transfer_select(self):

    # Loop through the files to find out when they were last updated.
    path = self.org_select
    for root, dirs, files in os.walk(path):
        for filename in files:
            filename = os.path.join(root, filename)

            # Get current time and subtract 24 hours from it to get 24 hour window
            now = time.time()
            old = now - 60*60*24

            # Get dates for new and modded files
            new_file = os.path.getmtime(filename)

            if now > new_file and new_file > old:
                shutil.move(filename, self.dst_select)

    # Connect to Database and save file check process
    conn = sqlite3.connect('move.db')
    with conn:
        cur = conn.cursor()
        cur.execute(""" SELECT unix FROM move_table""")    
        unix = int(time.time())
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        cur.execute("""INSERT INTO move_table(unix,datestamp) VALUES (?,?)""",(unix, date))
        conn.commit()
    messagebox.showinfo('Update','Operation Completed')
    onRefresh(self)
           
if __name__ == "__main__":
    pass
