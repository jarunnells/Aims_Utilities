#!/usr/bin/python3

# STANDARD LIBRARY IMPORTS
import os
import tkinter as tk
import tkinter.font as tk_font
from tkinter import (ttk, messagebox, filedialog)
from shutil import copy2
from datetime import datetime
from pathlib import Path
# THIRD PARTY IMPORTS

# LOCAL IMPORTS
from config import Colors, GUI_Setup
from rename import Photos as p_


class GUI(tk.Frame):

    def __init__(self, master, title: str, app_width: int, app_height: int, x: int, y: int):
        super(GUI, self).__init__(master=master)
        self.master = master
        master.title(string=title)
        master.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        master.resizable(
            width=GUI_Setup.RESIZABLE['width'],
            height=GUI_Setup.RESIZABLE['height']
        )
        master['bg'] = Colors.BLUE['hex']
        self.initialize_UI()

    def initialize_UI(self) -> None:
        root = tk.Tk()
        root.option_add('*tearOff', False)
        X = (root.winfo_screenwidth() / 2) \
            - ((APP_WIDTH := GUI_Setup.APP_WIDTH) / 2)
        Y = (root.winfo_screenheight() / 2) \
            - ((APP_HEIGHT := GUI_Setup.APP_HEIGHT) / 2)
        gui = GUI(
            master=root,
            title=GUI_Setup.TITLE,
            app_width=int(APP_WIDTH),
            app_height=int(APP_HEIGHT),
            x=X,
            y=Y
        )
        gui.mainloop()


def main():

    if p_.print_instructions():
        # dir_list_orig = p_.get_dir_list()
        # temp_dir = None
        temp_dir_FULL = None
        timestamp = f"[{'%m'}{'%d'}_{'%H'}{'%M'}{'%f'}]"

        try:
            p_.create_temp_dir(
                temp_dir := f"./temp{datetime.now().strftime(timestamp)}/")
            p_.copy_files(dir_list_orig := p_.get_dir_list(), temp_dir)
        except OSError as err:
            print(f'[ERROR] {err}')
        else:
            os.chdir(temp_dir)
        finally:
            temp_dir_FULL = os.getcwd()

        dir_list_temp = os.listdir() if os.getcwd() == temp_dir_FULL else None

        if dir_list_temp is not None:
            p_.rename_files(dir_list_temp)

    else:
        print('Please apply proper naming convention before running this utility!')


if __name__ == '__main__':
    main()
