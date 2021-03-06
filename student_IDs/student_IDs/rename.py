#!/usr/bin/python3

# STANDARD LIBRARY IMPORTS
import os
import tkinter as tk
import tkinter.font as tk_font
from tkinter import (ttk, messagebox, filedialog)
from shutil import copy2
from datetime import datetime
from pathlib import Path, PurePath
from typing import List
# THIRD PARTY IMPORTS

# LOCAL IMPORTS
from config import Messages


class Photos:

    def __init__(self,
                 root_path: str = None,
                 temp_path: str = None,
                 photo_path: str = None
                 ):
        self.root_path = root_path
        self.temp_path = temp_path
        self.photo_path = photo_path
        self.confirmed = None

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

    def get_dir_list(self, dir_path: str) -> List[str]:
        """Get directory file listing
        :returns dir_list: directory file listing
        """
        # dir_path = './test_files'
        return Path(dir_path).iterdir()

    def create_temp_dir(self, temp_dir: str) -> None:
        """Create temp directory to store renamed files
        :param temp_dir: directory string passed for validation
        """
        if not Path(temp_dir).is_dir():
            Path(temp_dir).mkdir(parents=True, )
        else:
            pass

    def copy_files(self, dir_list: str, temp_dir: str) -> None:
        """Copy orignial files into temp directory for renaming process
        :param dir_list: directory file list used in file copy process
        """
        count = 0
        for i, f in enumerate(dir_list, start=1):
            # if os.path.isfile(f):  # && !os.path.isdir(f):
            if Path(f).is_file():  # && !Path(f).is_dir():
                # copy2(f, f'./temp/{f}')
                copy2(f, f"{temp_dir}")
                count += 1
        print(f"Files moved: {count}")

    # TODO: add error handling
    def rename_files(self, dir_list: str, temp_dir: str) -> None:
        """Rename files method
        :param dir_list: Temp directory file list used in bulk renaming process
        """
        count = 0
        print(temp_dir)
        for i, f in enumerate(dir_list, start=1):
            try:
                print(f)
                # f_name, f_ext = os.path.splitext(f)
                f_name = PurePath(f).stem
                f_ext = PurePath(f).suffix
                pic_date, student, a_num = f_name.split('_')
                pic_date = pic_date.strip().zfill(4)
                student = student.strip()
                a_num = a_num.strip()
                a_num_masked = a_num[5:].strip()
            except ValueError as err:
                print(f"[ERROR] {err} -- {f}")
            except Exception as err:
                print(f"[ERROR] {err} -- {f}")

            try:
                f_name_NEW = f"{pic_date}_{student}_A-{a_num_masked}{f_ext}"
                # os.rename(f, f_name_NEW)
                Path(f).rename(f_name_NEW)
                count += 1
            except OSError as err:
                print(f"[ERROR] {err} -- {f_name_NEW}")
            except Exception as err:
                print(f"[ERROR] {err} -- {f_name_NEW}")

        print(f"Files renamed: {count}")
