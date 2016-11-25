# Python Ver:   3.6.0
#
# Author:       Tanvir Khondakar
#
# Purpose:      Phone book demo, showing the use of Tkinter
#
# Tested OS:    This code was written and tested to work on windows 10


from tkinter import *
import tkinter as tk


# Import of other modules:
import phonebook_gui
import phonebook_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our masterframe configuration
        self.master = master
        self.master.minsize(550,400)
        self.master.maxsize(550,400)

        # This CenterWindow will center our App on the screen
        phonebook_func.center_window(self,500,300)
        self.master.title("Tkinter Phonebook")
        self.master.configure(bg = '#F0F0F0')

        # This protocol method is a builtin Tkinter method to catch if
        # the user clicks on the upper corner 'x' on the windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a seperate module,
        # Keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root = mainloop()
