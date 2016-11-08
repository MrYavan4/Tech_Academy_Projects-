import os
from tkinter import *
import tkinter as tk
import sqlite3
import datetime

# Import other modules

import move_gui

#============================================================================================

# Catch if the user clicks on the windows upper-right 'X', to ensure that they want to close

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes the app
        self.master.destroy()
        os_exit(0)


#============================================================================================
    

def create_db(self):
    conn = sqlite3.connect('move.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_move( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_FileName TEXT, \
            col_Date DATETIME, \
            );")
        # Must coomit() to save changes & close the database connection
        conn.commit()
    conn.close()
    first_run(self)
    
def first_run(self):
    conn = sqlite3.connect('move.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            print('Files have not been updated')

def file_check(self):
    now = datetime.datetime.now
    now.strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('move.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO table (coL_FileName, col_Date) VALUES (?,?')",
               ("name", now))

if __name__ == "__main__":
    pass
