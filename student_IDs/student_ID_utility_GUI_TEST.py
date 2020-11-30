# STANDARD LIBRARY IMPORTS
import tkinter as tk
import tkinter.font as tk_font  # tkFont
from tkinter import (ttk, messagebox)

# THIRD PARTY IMPORTS

# LOCAL IMPORTS

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

GUI_DIM = {"width": 700, "height": 450}


class GUI(tk.Frame):
    global GUI_DIM
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title("Student ID Utility")
        master.resizable(width=False, height=False)
        master.geometry(width=GUI_DIM['width'], height=GUI_DIM['height'])
        master['bg'] = COLORS['antique_white']['py_name']

        self.frame_leftTop = tk.Frame(master, bg="red", height=225, width=150)
        self.frame_leftBottom = tk.Frame(
            master, bg="green", height=225, width=150)
        self.frame_rightFull = tk.Frame(
            master, bg="blue", height=150, width=350)

        # self.frame_leftTop.grid(row=5, column=5, rowspan=15, columnspan=10, sticky=tk.N+tk.W)
        # self.frame_leftBottom.grid(row=20, column=5, rowspan=15, columnspan=10, sticky=tk.S+tk.W)
        # self.frame_rightFull.grid(row=5, column=20, rowspan=40, columnspan=40, sticky=tk.E)

        self.frame_rightFull.pack(side="right", fill="both")
        self.frame_leftTop.pack(side="top", fill="both")
        self.frame_leftBottom.pack(
            side="bottom", fill="both", after=self.frame_leftTop)

        self.tree = None


if __name__ == '__main__':
    root = tk.Tk()
    root.option_add('*tearOff', False)
    gui = GUI(master=root)
    gui.mainloop()
