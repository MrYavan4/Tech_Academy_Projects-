from tkinter import *
from tkinter.ttk import *
import tkinter as tk

# Import other modules:
import move_gui
import move_function

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(550,350)
        self.master.maxsize(550,350)

        # Title and Background color
        self.master.title("Move Files Program")
        self.master.configure(bg = "#eeeeff")

        move_gui.load_gui(self)
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root = mainloop()



