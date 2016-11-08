# Python version 3.6
#
# Author: Tanvir Khondakar


from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askdirectory
import os

#import Move_Files_Drill

import Move_Files_Drill
import function_move

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("File Transfer")
        
        self.pack(fill = BOTH, expand = 1)

        self.lbl_file = tk.Label(self, text = " Last File Update: ")
        self.lbl_file.grid(row = 0, column = 1, padx =(27,0), pady = (10,0), sticky = N+W)

        self.txt_file = tk.Entry(self, textvariable = "")
        self.txt_file.grid(row = 1, column = 1, padx =(27,0), pady = (10,0), sticky = N+W)

        self.lbl_select = tk.Label(self, text = " Select from which folder to transfer files from: ")
        self.lbl_select.grid(row = 2, column = 1, padx =(27,0), pady = (10,0), sticky = N+W)

        Org_Button = ttk.Button(self, text = "Select Folder", command = self.org_select)
        Org_Button.grid(row = 3, column = 1, rowspan = 1, columnspan = 2,
                        padx =(30,40), pady = (10,0), sticky = N+E+W)

        self.lbl_select = tk.Label(self, text = " Select from which folder to transfer files from: ")
        self.lbl_select.grid(row = 4, column = 1, padx =(27,0), pady = (10,0), sticky = N+W)

        Dst_Button = ttk.Button(self, text = "Select Folder", command = self.dst_select)
        Dst_Button.grid(row = 5, column = 1, rowspan = 1, columnspan = 2,
                        padx =(30,40), pady = (10,0), sticky = N+E+W)

        self.lbl_select = tk.Label(self, text = " Click to Transfer Files: ")
        self.lbl_select.grid(row = 6, column = 1, padx =(27,0), pady = (10,0), sticky = N+W)

        Transfer_Button = ttk.Button(self, text = "Transfer", command = self.transfer_select)
        Transfer_Button.grid(row = 7, column = 1, rowspan = 1, columnspan = 2,
                        padx =(30,40), pady = (10,0), sticky = N+E+W)

    
    def org_select(self):
        root.org_path = askdirectory()
        org_path = root.org_path
        return org_path
    
    def dst_select(self):
        root.dst_path = askdirectory()
        dst_path = root.dst_path 
        return dst_path


    def transfer_select(self):
        # Loop through the files to find out when they were last updated.
        
        for root, dirs, files in os.walk(org_path):
            for filename in files:
                filename = os.path.join(root, filename)

                # Get today's date
                today_date = datetime.date.today()

                # Get dates for new and modded files
                new_file = (datetime.date.fromtimestamp(os.stat(filename).st_ctime))
                mod_file = (datetime.date.fromtimestamp(os.stat(filename).st_mtime))

                if mod_file == today_date or new_file == today_date:
                    shutil.move(filename, dst_path)
                    print('Files Transfered')
                else:
                    print('No files to update today')   

root = Tk()

app = Window(root)

root.mainloop()
