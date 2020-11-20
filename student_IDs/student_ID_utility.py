# STANDARD LIBRARY IMPORTS
try:
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk
except ImportError:
    import Tkinter as tk
    import tkFont
    import ttk
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
        # master.geometry("700x450")
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
    size = { "width": 700, "height": 450}
    root = tk.Tk()
    root.minsize(size["width"], size["height"])
    root.maxsize(size["width"], size["height"])
    gui = GUI(master=root)
    gui.mainloop()
