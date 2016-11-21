from tkinter import *
import tkinter as tk
import os
from tkinter import filedialog
from tkinter import messagebox
import datetime
import shutil
import sqlite3


class Move_GUI():
    def __init__(self, master):
        self.master = master
        master.title("File Transfer")

        master.minsize(width=300, height=400)
        master.maxsize(width=300, height=400)

        # Buttons and Labels:
        self.label_main = Label(master, text="Transfer Files")
        self.label_main.grid(row = 0, column = 0, padx =(20,0), pady = (10,0))

        self.label_update = Label(master, text="Check when files were last tranferred:")
        self.label_update.grid(row = 1, column = 0, padx =(20,0), pady = (10,0))
        self.button_update = tk.Button(master, text = "Check Update",command = lambda: check_update(self))
        self.button_update.grid(row = 2, column = 0, padx =(20,0), pady = (10,0))

        self.label_select_org = Label(master, text="Select Orgin Folder:")
        self.label_select_org.grid(row = 3, column = 0, padx =(20,0), pady = (10,0))
        self.button1 = tk.Button(master, text = "Select Folder",command = lambda: org_select(self))
        self.button1.grid(row = 4, column = 0, padx =(20,0), pady = (20,0))

        self.label_select_dst = Label(master, text="Select Destination Folder:")
        self.label_select_dst.grid(row = 5, column = 0, padx =(20,0), pady = (10,0))
        self.button2 = tk.Button(master, text = "Select Folder", command = lambda: dst_select(self))
        self.button2.grid(row = 6, column = 0, padx =(20,0), pady = (20,0))

        self.label_transfer = Label(master, text="Click to transfer files:")
        self.label_transfer.grid(row = 7, column = 0, padx =(20,0), pady = (10,0))
        self.button3 = tk.Button(master, text = "Transfer File", command = lambda: transfer_select(self))
        self.button3.grid(row = 8, column = 0, padx =(20,0), pady = (20,0))


        # Create Database:
        def create_db(self):
            conn = sqlite3.connect('move.db')
            with conn:
                c = conn.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS move_table(datestamp TEXT)')
                conn.commit()
            conn.close()

        create_db(self)

        #Functions:

        def check_update(self):
            conn = sqlite3.connect('move.db')
            with conn:
                c = conn.cursor()
                c.execute("SELECT * FROM move_table")
                row = c.fetchone()
                if row is not None:
                  self.labl = tk.Label(master, text="{}".format(row))
                  self.labl.grid(row = 3, column = 0, padx =(20,0), pady = (10,0))
                  row = c.fetchone()
                else:
                     messagebox.showinfo('Update','No Files have been transferred recently. Transfer files first')
            conn.close()

        def org_select(self):
            self.org_select = filedialog.askdirectory()
            return self.org_select
            
        def dst_select(self):
            self.dst_select = filedialog.askdirectory()
            return self.dst_select

        def transfer_select(self):

            # Loop through the files to find out when they were last updated.

            path = self.org_select
            for root, dirs, files in os.walk(path):
               for filename in files:
                    filename = os.path.join(root, filename)

                    # Get today's date
                    today_date = datetime.date.today()
                    
                    # Get dates for new and modded files
                    new_file = (datetime.date.fromtimestamp(os.stat(filename).st_ctime))
                    mod_file = (datetime.date.fromtimestamp(os.stat(filename).st_mtime))

                    if mod_file == today_date or new_file == today_date:
                        shutil.move(filename, self.dst_select)
                        messagebox.showinfo('Update','Files Have been Transferred')
                        conn = sqlite3.connect('move.db')
                        with conn:
                            c = conn.cursor()
                            date = datetime.datetime.fromtimestamp(filename).strftime('%Y-%m-%d %H:%M:%S')
                            c.execute("""INSERT INTO move_table(datestamp) VALUE(?)""",
                                      (date))
                            conn.close()  
                    else:
                        messagebox.showinfo('Update','No Files to transfer today')

root = Tk()
my_gui =  Move_GUI(root)
root.mainloop()
