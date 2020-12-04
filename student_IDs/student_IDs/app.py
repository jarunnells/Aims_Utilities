#!/usr/bin/python3

# STANDARD LIBRARY IMPORTS
import tkinter as tk
import tkinter.font as tk_font
from tkinter import (ttk, messagebox)

# THIRD PARTY IMPORTS

# LOCAL IMPORTS
# from rename_files import ...


COLORS = {
    "light_steel_blue": {
        "py_name": "light steel blue",
        "hex": "#B0C4DE",
        },
    "light_coral": {
        "py_name": "light coral",
        "hex": "#F08080",
        },
    "lavender": {
        "py_name": "lavender",
        "hex": "#E6E6FA",
        },
    "antique_white": {
        "py_name": "antique white",
        "hex": "#FAEBD7",
        },
}


class GUI(tk.Frame):

    def __init__(self, master, title, app_width, app_height, x, y):
        super(GUI, self).__init__(master=master)
        self.master = master
        master.title(string=title)
        master.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        master.resizable(width=False, height=False)
        master['bg'] = "#B0C4DE"
        self.initialize_UI()

    def initialize_UI(self):
        pass


def main():
    root = tk.Tk()
    root.option_add('*tearOff', False)
    TITLE = "Cafe POS Database Management"
    SCREEN_WIDTH = root.winfo_screenwidth()
    SCREEN_HEIGHT = root.winfo_screenheight()
    APP_WIDTH = 650
    APP_HEIGHT = 625
    X = (SCREEN_WIDTH / 2) - (APP_WIDTH / 2)
    Y = (SCREEN_HEIGHT / 2) - (APP_HEIGHT / 2)
    gui = GUI(
        master=root,
        title=TITLE,
        app_width=APP_WIDTH,
        app_height=APP_HEIGHT,
        x=X,
        y=Y
    )
    gui.mainloop()


if __name__ == '__main__':
    main()
