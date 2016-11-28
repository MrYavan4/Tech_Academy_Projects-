# Python Ver:   3.6.0
#
# Author:       Tanvir Khondakar
#
# Purpose:      File Transfer Program gui using tkinter
#
# Tested OS:    This code was written and tested to work on windows

from tkinter import *
from tkinter.ttk import *
import tkinter as tk


# Import other modules:

import move_main
import move_function


def load_gui(self):

    # Labels
    self.lbl_origin = tk.Label(self.master, text = 'Origin Folder:')
    self.lbl_origin.grid(row = 0, column = 0,
                        padx =(20, 10), pady =(10, 0), sticky = N+W)
    self.lbl_dst = tk.Label(self.master, text = 'Destination Folder:')
    self.lbl_dst.grid(row = 3, column = 0,
                        padx =(20, 10), pady =(10, 0), sticky = N+W)
    self.lbl_transfer = tk.Label(self.master, text = 'Last Files Transfers Performed:')
    self.lbl_transfer.grid(row = 0, column = 2,
                        padx =(0, 10), pady =(10, 0), sticky = N+W)

    # Scroll Bar

    self.scrollbar1 = Scrollbar(self.master, orient = VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection = 0,
                            yscrollcommand = self.scrollbar1.set)
    self.scrollbar1.config(command = self.lstList1.yview)
    self.scrollbar1.grid(row = 1, column = 5, rowspan = 7, columnspan = 1,
                         padx = (0,0), pady = (0,0), sticky = N+E+S)
    self.lstList1.grid(row = 1, column = 2, rowspan = 7, columnspan = 3,
                         padx = (0,0), pady = (0,0), sticky = N+E+S+W)

    #Buttons

    self.btn_add = tk.Button(self.master, width = 12, height = 2, text = "Select Folder",
                             command = lambda: move_function.org_select(self))
    self.btn_add.grid(row = 2, column = 0, padx = (20,10), pady = (20,10), sticky = W)

    self.btn_update = tk.Button(self.master, width = 12, height = 2, text = "Select Folder",
                             command = lambda: move_function.dst_select(self))
    self.btn_update.grid(row = 5, column = 0, padx = (20,10), pady = (20,10), sticky = W)

    self.btn_delete = tk.Button(self.master, width = 12, height = 2, text = "Transfer",
                             command = lambda: move_function.transfer_select(self))
    self.btn_delete.grid(row = 8, column = 2, padx = (25,0), pady = (20,10), sticky = W)

    self.btn_close = tk.Button(self.master, width = 12, height = 2, text = "Close",
                             command = lambda: move_function.ask_quit(self))
    self.btn_close.grid(row = 8, column = 3,columnspan = 1, padx = (25,0), pady = (20,10), sticky = E)

    move_function.create_db(self)
    move_function.onRefresh(self)

