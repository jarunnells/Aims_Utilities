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
    KWARGS_FRAME = {
        "padding": (5,),
        "relief": tk.FLAT,
        "borderwidth": None,
        "width": None,
        "height": None,
        "style": None,
    }
    KWARGS_PACK = {
        "expand": tk.YES,
        "fill": tk.BOTH,
        "padx": 5,
        "pady": 5,
        "ipadx": 5,
        "ipady": 5,
    }
    KWARGS_GRID_INIT = {
        "padx": 5,
        "pady": 5,
        "ipadx": 5,
        "ipady": 5,
    }
    KWARGS_GRID_HEADER = {
        "column": None,
        "row": None,
        "sticky": None,  # "sticky": tk.N+tk.S+tk.E+tk.W
        "columnspan": None,
    }
    KWARGS_GRID_NAV = {
        "column": None,
        "row": None,
        "sticky": None,  # "sticky": tk.N+tk.S+tk.E+tk.W
        "columnspan": None,
    }
    KWARGS_GRID_INTERFACE_PARENT = {
        "column": None,
        "row": None,
        "sticky": None,  # "sticky": tk.N+tk.S+tk.E+tk.W
        "columnspan": None,
    }
    KWARGS_GRID_INTERFACE_CHILD_RENAME = {
        "column": None,
        "row": None,
        "sticky": None,  # "sticky": tk.N+tk.S+tk.E+tk.W
        "columnspan": None,
    }
    KWARGS_GRID_INTERFACE_CHILD_PHOTO = {
        "column": None,
        "row": None,
        "sticky": None,  # "sticky": tk.N+tk.S+tk.E+tk.W
        "columnspan": None,
    }
    SIDES = (tk.TOP, tk.LEFT, tk.RIGHT, None, None,)
    CNF = KWARGS_PACK


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
