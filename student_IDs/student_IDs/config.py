#!/usr/bin/python3

# STANDARD LIBRARY IMPORTS
import tkinter as tk
from tkinter import (ttk, messagebox, font as tk_font)
from pathlib import Path
from typing import (Dict, List, Iterator, Tuple, Any)


class GUI_Setup:
    TITLE = "Student ID Manager"
    APP_WIDTH = 450
    APP_HEIGHT = 450
    RESIZABLE = {"width": False, "height": True}
    COLORS = {
        "BLUE": {
            "py_name": "light steel blue",
            "hex": "#B0C4DE",
        },
        "CORAL": {
            "py_name": "light coral",
            "hex": "#F08080",
        },
        "LAVENDER": {
            "py_name": "lavender",
            "hex": "#E6E6FA",
        },
        "WHITE": {
            "py_name": "antique white",
            "hex": "#FAEBD7",
        },
    }
    FONTS = {
        "DEFAULT": {
            "family": "JetBrains Mono",
            "size": 12,
            "weight": tk.NORMAL,
        },
        "MESSAGEBOX": {
            "family": "Courier",
            "size": 12,
            "weight": tk.NORMAL,
        },
    }
    THEMES: Tuple[str, ...] = (
        "default", "classic", "clam", "aqua", "alt",
    )


class Frame_Setup:
    KWARGS_FRAME_INIT = {
        "padding": (5,),
        "relief": tk.FLAT,
        "borderwidth": None,
    }
    KWARGS_FRAME_CONTAINER = {
        "width": None,
        "height": None,
        "style": "Container.TFrame",
    }
    KWARGS_FRAME_HEADER = {
        "width": None,
        "height": None,
        "style": "Header.TFrame",
    }
    KWARGS_FRAME_NAV = {
        "width": None,
        "height": None,
        "style": "Navigation.TFrame",
    }
    KWARGS_FRAME_INTERFACE_PARENT = {
        "width": None,
        "height": None,
        "style": "Interface.TFrame",
    }    
    KWARGS_FRAME_INTERFACE_CHILD_RENAME = {
        "width": None,
        "height": None,
        "style": "Rename.TFrame",
    }
    KWARGS_FRAME_INTERFACE_CHILD_PHOTO = {
        "width": None,
        "height": None,
        "style": "Photo.TFrame",
    }
    KWARGS_PACK_INIT = {
        "padx": 5,
        "pady": 5,
        "ipadx": 5,
        "ipady": 5,
    }
    KWARGS_PACK_CONTAINER = {
        "side": tk.TOP,
        "expand": True,
        "fill": tk.BOTH,
    }
    KWARGS_PACK_HEADER = {
        "side": tk.TOP,
        "expand": True,
        "fill": tk.X,
    }
    KWARGS_PACK_NAV = {
        "side": tk.LEFT,
        "expand": True,
        "fill": tk.Y,
    }
    KWARGS_PACK_INTERFACE_PARENT = {
        # "side": tk.LEFT,
        "side": tk.RIGHT,
        "expand": True,
        "fill": tk.BOTH,
    }
    KWARGS_GRID_INIT = {
        "padx": 5,
        "pady": 5,
        "ipadx": 5,
        "ipady": 5,
    }
    KWARGS_GRID_HEADER = {
        "column": 1,
        "row": 0,
        "sticky": tk.N,
        # "sticky": tk.N + tk.S + tk.E + tk.W,
        "columnspan": 2,
    }
    KWARGS_GRID_NAV = {
        "column": 0,
        "row": 0,
        "sticky": tk.N + tk.S + tk.W,
        # "sticky": tk.N + tk.S + tk.E + tk.W,
        "columnspan": 1,
    }
    KWARGS_GRID_INTERFACE_PARENT = {
        "column": 1,
        "row": 0,
        # "sticky": tk.N + tk.W,
        "sticky": tk.N + tk.S + tk.E + tk.W,
        "columnspan": 1,
    }
    KWARGS_GRID_INTERFACE_CHILD_RENAME = {
        "column": 0,
        "row": 0,
        "sticky": tk.N + tk.S + tk.E + tk.W,
        "columnspan": 1,
    }
    KWARGS_GRID_INTERFACE_CHILD_PHOTO = {
        "column": 0,
        "row": 0,
        "sticky": tk.N + tk.S + tk.E + tk.W,
        "columnspan": 1,
    }
    SIDES = (tk.TOP, tk.LEFT, tk.RIGHT, None, None,)
    CNF = KWARGS_PACK_INIT


class Button_Setup:
    KWARGS_GRID_INIT = {
        "padx": 5,
        "pady": 5,
        "ipadx": 5,
        "ipady": 5,
    }
    KWARGS_GRID_MSGBOX_CONF = {
        "row": 1,
        "column": 0,
        "sticky": tk.E}
    KWARGS_GRID_MSGBOX_CXL = {
        "row": 1,
        "column": 1,
        "sticky": tk.W}
    KWARGS_GRID_ = {}


class Label_Setup:
    KWARGS_GRID_INIT = {
        "padx": 5,
        "pady": 5,
        "ipadx": 5,
        "ipady": 5,
    }
    KWARGS_GRID_MSGBOX = {
        "row": 0,
        "column": 0,
        "columnspan": 2,
        "sticky": tk.N+tk.S+tk.E+tk.W
    }
    KWARGS_GRID_ = {}


class Entry_Setup:
    KWARGS_GRID_INIT = {
        "padx": 5,
        "pady": 5,
        "ipadx": 5,
        "ipady": 5,
    }
    KWARGS_GRID_ = {}


class FS_Setup:
    DIR_OPTS = {
        "initialdir": None,
        "title": "Select Directory",
        "initialfile": None,
        "mustexist": True,
    }
    FILE_OPTS = {
        "initialdir": None,
        "title": "Select Image File",
        "filetypes": [
            ("jpeg files", "*.jpeg"),
            ("jpg files", "*.jpg"),
            ("png files", "*.png")
        ],
        "defaultextension": "*.png",
    }
    CANCELLED = "Dialog Cancelled..."
    INSTRUCTIONS = """REQUIRED FILE NAME FORMAT:
  (photo_date)_(student_last-student_first)_(A_number).jpg

    [EXAMPLE]
          1025_Aardvark-Arthur_A00123456.jpg
    """
    CONFIRMATION = "All files named properly?"


class Messages:
    INSTRUCTIONS: Dict[str, str] = {
        "title": "CONFIRM PROPER NAMING CONVENTION!",
        "message": "Please confirm proper file naming convention (ALL files):" \
        f"\n\n{FS_Setup.INSTRUCTIONS}\n\n{FS_Setup.CONFIRMATION}"
        }
