# STANDARD LIBRARY IMPORTS
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from tkinter import messagebox

# CUSTOM LIBRARY IMPORTS

COLORS = {
    "light_steel_blue": {"py_name": "light steel blue", "hex": "#B0C4DE", "rgb": (176, 196, 222)},
    "light_coral": {"py_name": "light coral", "hex": "#F08080", "rgb": (240, 128, 128)},
    "lavender": {"py_name": "lavender", "hex": "#E6E6FA", "rgb": (230, 230, 250)},
    "antique_white": {"py_name": "antique white", "hex": "#FAEBD7", "rgb": (250, 235, 215)},
}


class GUI(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title("Student ID Utility")
        master.geometry("700x425")
        master['bg'] = COLORS['antique_white']['py_name']


if __name__ == '__main__':
    root = tk.Tk()
    gui = GUI(master=root)
    gui.mainloop()