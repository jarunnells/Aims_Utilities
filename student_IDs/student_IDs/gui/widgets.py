#!/usr/bin/python3

# STANDARD LIBRARY IMPORTS
import tkinter as tk
import tkinter.font as tk_font
from tkinter import (ttk, messagebox)

# THIRD PARTY IMPORTS

# LOCAL IMPORTS
# from rename_files import ...


class GUI_Window:

    def __init__(self, parent, title, geometry, resizable, background,
                 *args, **kwargs):
        self.parent = parent
        self.parent.title(title)
        self.parent.geometry(geometry)  # 'WIDTHxHEIGHT+X+Y'
        self.parent.resizable(resizable)
        self.parent.mainloop()


class GUI_Button:

    def __init__(self, parent, text, width, justify, state, underline,
                 textVariable, style, command, *args, **kwargs):
        self.button = ttk.Button(self, parent)
        pass


class GUI_Label:

    def __init__(self, parent, *args, **kwargs):
        self.label = ttk.Label(self, parent)
        pass


class GUI_Entry:

    def __init__(self, parent, *args, **kwargs):
        self.entry = ttk.Entry(self, parent)
        pass


class GUI_Combobox:

    def __init__(self, parent, *args, **kwargs):
        self.entry = ttk.Combobox(self, parent)
        pass


class GUI_Scrollbar:

    def __init__(self, parent, *args, **kwargs):
        self.scrollbar = ttk.Scrollbar(self, parent)
        pass


class GUI_Progressbar:

    def __init__(self, parent, *args, **kwargs):
        self.scrollbar = ttk.Progressbar(self, parent)
        pass
