#!/usr/bin/python3

# STANDARD LIBRARY IMPORTS
import os
import tkinter as tk
import tkinter.font as tk_font
from tkinter import (ttk, messagebox, filedialog)
from shutil import copy2
from datetime import datetime
from pathlib import Path
from typing import List
# THIRD PARTY IMPORTS

# LOCAL IMPORTS
from config import Messages


class Photos:

    def __init__(self):
        pass

    def instructions(self) -> bool:
        """Print Initial Instructions
        :returns confirmed: boolean control variable -> True=continue, False=exit
        """
        # usr_prompt = input('All files named properly? [Y/N] >>: ')
        # confirmed = True if usr_prompt.lower() == 'y' else False
        confirmed = messagebox.askyesno(
            title=Messages.INSTRUCTIONS['title'],
            message=Messages.INSTRUCTIONS['message'],
        )

        return confirmed

    def get_dir_list(self) -> List[str]:
        """Prompt for directory and get file list
        :returns dir_list: directory file listing
        """
        # dir_path = './test_files'
        temp = './test_files'
        dir_path = input(f'Directory PATH {temp} >>: ')
        os.chdir(dir_path)

        return os.listdir()

    def create_temp_dir(self, temp_dir: str) -> None:
        """Create temp directory to store renamed files
        :param temp_dir: directory string passed for validation
        """
        if not os.path.isdir(temp_dir):
            os.makedirs(temp_dir)
        else:
            pass

    def copy_files(self, dir_list: str, temp_dir: str) -> None:
        """Copy orignial files into temp directory for renaming process
        :param dir_list: directory file list used in file copy process
        """
        count = 0
        for i, f in enumerate(dir_list, start=1):
            if os.path.isfile(f):  # && !os.path.isdir(f):
                # copy2(f, f'./temp/{f}')
                copy2(f, f'{temp_dir}{f}')
                count += 1
        print(f'Files moved: {count}')

    def rename_files(self, dir_list: str) -> None:
        """Rename files method
        :param dir_list: Temp directory file list used in bulk renaming process
        """
        count = 0
        for i, f in enumerate(dir_list, start=1):
            f_name, f_ext = os.path.splitext(f)
            pic_date, student, a_num = f_name.split('_')
            pic_date = pic_date.strip().zfill(4)
            student = student.strip()
            a_num = a_num.strip()
            a_num_masked = a_num[5:].strip()

            try:
                f_name_NEW = f'{pic_date}_{student}_A-{a_num_masked}{f_ext}'
                os.rename(f, f_name_NEW)
                count += 1
            except OSError as err:
                print(f'[ERROR] {err}')

        print(f'Files renamed: {count}')
