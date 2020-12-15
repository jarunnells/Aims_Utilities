#!/usr/bin/python3

# STANDARD LIBRARY IMPORTS
from tkinter import filedialog
from pathlib import Path
# LOCAL IMPORTS
from config import FS_Setup


class File_Sys:
    # global HOME_DIR, INIT_DIR
    # HOME_DIR = Path.home()
    # INIT_DIR = Path(HOME_DIR, 'Desktop')
    DEFAULT = Path.home()

    def __init__(self,
                 home_dir=DEFAULT,
                 init_dir=DEFAULT,
                 ):
        self.home_dir = home_dir
        self.init_dir = init_dir

    def ask_dir(self) -> str:
        """Ask for a directory, and return the file name"""
        options = FS_Setup.DIR_OPTS
        options['initialdir'] = self.init_dir
        dir_path = filedialog.askdirectory(**options)
        print(dir_path) if dir_path else print(f"[1] {FS_Setup.CANCELLED}")
        return dir_path if dir_path else None

    def ask_file(self, mode='r') -> str:
        """Ask for a filename to open, and returned the opened file"""
        options = FS_Setup.FILE_OPTS
        options['initialdir'] = self.init_dir
        path = filedialog.askopenfile(mode=mode, **options)
        print(path.name) if path else print(f"[2] {FS_Setup.CANCELLED}")
        return path if path else None

    def ask_filename(self) -> str:
        """Ask for a filename to open"""
        options = FS_Setup.FILE_OPTS
        options['initialdir'] = self.init_dir
        file_path = filedialog.askopenfilename(**options)
        print(file_path) if file_path else print(f"[3] {FS_Setup.CANCELLED}")
        return file_path if file_path else None
