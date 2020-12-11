#!/usr/bin/python3

# STANDARD LIBRARY IMPORTS
import tkinter as tk
import tkinter.font as tk_font
from tkinter import (ttk, messagebox)
from pathlib import Path
# THIRD PARTY IMPORTS

# LOCAL IMPORTS


class GUI_Setup:
    TITLE = "Cafe POS Database Management"
    APP_WIDTH = 650
    APP_HEIGHT = 625
    RESIZABLE = {"width": False, "height": True}


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
    CONFIRMATION = "All files named properly? [Y/N] >>: "


class Colors:
    BLUE = {
        "py_name": "light steel blue",
        "hex": "#B0C4DE",
    }
    CORAL = {
        "py_name": "light coral",
        "hex": "#F08080",
    }
    LAVENDER = {
        "py_name": "lavender",
        "hex": "#E6E6FA",
    }
    WHITE = {
        "py_name": "antique white",
        "hex": "#FAEBD7",
    }
