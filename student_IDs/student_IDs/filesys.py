#!/usr/bin/python3

# STANDARD LIBRARY IMPORTS
from tkinter import filedialog
from pathlib import Path
# THIRD PARTY IMPORTS

# LOCAL IMPORTS
from config import FS_Setup


class File_Sys:
    def __init__(self):
        self.home_dir = Path.home()
        self.initial_directory = Path(self.home_dir, 'Desktop')

    def ask_dir(self):
        """Ask for a directory, and return the file name"""
        options = FS_Setup.DIR_OPTS
        options['initialdir'] = self.initial_directory
        path_1 = filedialog.askdirectory(**options)
        print(path_1) if path_1 else print(f"[1] {FS_Setup.CANCELLED}")

    def ask_file(self):
        """Ask for a filename to open, and returned the opened file"""
        options = FS_Setup.FILE_OPTS
        options['initialdir'] = self.initial_directory
        path_2 = filedialog.askopenfile(mode='r', **options)
        print(path_2.name) if path_2 else print(f"[2] {FS_Setup.CANCELLED}")

    def ask_filename(self):
        """Ask for a filename to open"""
        options = FS_Setup.FILE_OPTS
        options['initialdir'] = self.initial_directory
        path_3 = filedialog.askopenfilename(**options)
        print(path_3) if path_3 else print(f"[3] {FS_Setup.CANCELLED}")
