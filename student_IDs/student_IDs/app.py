#!/usr/bin/python3

# STANDARD LIBRARY IMPORTS
import os
import tkinter as tk
from tkinter import (ttk, messagebox, filedialog, font as tk_font)
from shutil import copy2
from datetime import datetime
from pathlib import Path
# THIRD PARTY IMPORTS

# LOCAL IMPORTS
from config import (GUI_Setup, Frame_Setup)
from rename import Photos
from filesys import File_Sys

# p_ = Photos()
# fs_ = File_Sys()


class GUI(tk.Frame):
    # def __init__(self, *args, **kwargs):
    def __init__(self, master,
                 title: str,
                 app_width: int,
                 app_height: int,
                 x: int,
                 y: int
                 ):
        super(GUI, self).__init__(master=master)
        self.master = master
        self.master.title(string=title)
        self.master.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.master.resizable(
            width=GUI_Setup.RESIZABLE['width'],
            height=GUI_Setup.RESIZABLE['height']
        )
        # self.master['bg'] = GUI_Setup.COLORS['BLUE']['hex']
        self.default_font = tk_font.Font(
            family=GUI_Setup.FONTS['DEFAULT']['family'],
            size=GUI_Setup.FONTS['DEFAULT']['size'],
            weight=GUI_Setup.FONTS['DEFAULT']['weight'],
        )
        self.p_ = Photos(root_path=Path.cwd())
        self.fs_ = File_Sys(
            home_dir=Path.home(),
            init_dir=Path(Path.home(), 'Desktop')
        )
        self.container_list = []
        self.initialize_UI()

    def initialize_UI(self) -> None:
        """WIDGET CONFIGURATIONS"""
        self.create_styles()
        self.create_frames()
        self.create_buttons()

    def create_styles(self):
        """create_styles [summary]

        [extended_summary]
        """
        self.style = ttk.Style()
        self.style.theme_use(themename=GUI_Setup.THEMES[2])
        self.style.configure(
            "TFrame",
            relief=tk.FLAT,
        )
        self.style.configure(
            "Container.TFrame",
            background=GUI_Setup.COLORS['BLUE']['hex'],
        )
        self.style.configure(
            "Header.TFrame",
            background=GUI_Setup.COLORS['CORAL']['hex'],
        )
        self.style.configure(
            "Navigation.TFrame",
            background=GUI_Setup.COLORS['LAVENDER']['hex'],
        )
        self.style.configure(
            "Interface.TFrame",
            background=GUI_Setup.COLORS['WHITE']['hex'],
        )
        self.style.configure(
            "Rename.TFrame",
            background=GUI_Setup.COLORS['WHITE']['hex'],
        )
        self.style.configure(
            "Photo.TFrame",
            background=GUI_Setup.COLORS['WHITE']['hex'],
        )

    def create_frames(self):
        """create_frames >> Create GUI Frames

        [extended_summary]
        """
        # MAIN CONTAINER
        self.container = ttk.Frame(master=self.master, padding=(10,))
        self.container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.container.grid_rowconfigure(index=0, weight=1)
        self.container.grid_columnconfigure(index=0, weight=1)

        # INSTANTIATE FRAMES -> SUB-CONTAINERS
        # self.frame_header = ttk.Frame(master=self.container)
        self.frame_nav = ttk.Frame(master=self.container)
        self.frame_interface_parent = ttk.Frame(master=self.container)
        self.frame_interface_child_rename = ttk.Frame(master=self.frame_interface_parent)
        self.frame_interface_child_photo = ttk.Frame(master=self.frame_interface_parent)

        # APPLY STYLING
        self.container.configure(style="Container.TFrame")
        # self.frame_header.configure(style="Header.TFrame")
        self.frame_nav.configure(style="Navigation.TFrame")
        self.frame_interface_parent.configure(style="Interface.TFrame")
        self.frame_interface_child_rename.configure(style="Rename.TFrame")
        self.frame_interface_child_photo.configure(style="Photo.TFrame")

        # self.frame_header.grid({
        #     **Frame_Setup.KWARGS_GRID_INIT,
        #     **Frame_Setup.KWARGS_GRID_HEADER
        # })
        self.frame_nav.grid({
            **Frame_Setup.KWARGS_GRID_INIT,
            **Frame_Setup.KWARGS_GRID_NAV
        })
        self.frame_interface_parent.grid({
            **Frame_Setup.KWARGS_GRID_INIT,
            **Frame_Setup.KWARGS_GRID_INTERFACE_PARENT
        })
        self.frame_interface_child_rename.grid({
            **Frame_Setup.KWARGS_GRID_INIT,
            **Frame_Setup.KWARGS_GRID_INTERFACE_CHILD_RENAME
        })
        self.frame_interface_child_photo.grid({
            **Frame_Setup.KWARGS_GRID_INIT,
            **Frame_Setup.KWARGS_GRID_INTERFACE_CHILD_PHOTO
        })

        # FRAMES = [
        #     self.frame_header,
        #     self.frame_nav,
        #     self.frame_interface_parent,
        #     self.frame_interface_child_rename,
        #     self.frame_interface_child_photo,
        # ]

        # for i, frame in enumerate(FRAMES):
        #     frame.pack(cnf=Frame_Setup.CNF, side=Frame_Setup.SIDES[i])

        '''
        FRAMES = {
            "self.frame_header": {
                "expand": tk.YES,
                "fill": tk.BOTH,
                "side": tk.TOP,
                "padx": 5,
                "pady": 5,
            },
            "self.frame_nav": {
                "expand": tk.YES,
                "fill": tk.BOTH,
                "side": tk.LEFT,
                "padx": 5,
                "pady": 5,
            },
            "self.frame_interface_parent": {
                "expand": tk.YES,
                "fill": tk.BOTH,
                "side": tk.RIGHT,
                "padx": 5,
                "pady": 5,
            },
            "self.frame_interface_child_rename": {
                "expand": tk.YES,
                "fill": tk.BOTH,
                "side": tk.RIGHT,
                "padx": 5,
                "pady": 5,
            },
            "self.frame_interface_child_photo": {
                "expand": tk.YES,
                "fill": tk.BOTH,
                "side": tk.RIGHT,
                "padx": 5,
                "pady": 5,
            },
            "self.frame_footer": {
                "expand": tk.YES,
                "fill": tk.BOTH,
                "side": tk.BOTTOM,
                "padx": 5,
                "pady": 5,
            }
        }
        '''

    def create_buttons(self):
        """create_buttons >> Add button widgets to frame(s)

        [extended_summary]
        """
        _PARENT = (self.container, self.master, self.frame_nav)

        # BUTTON 01 -> Set directory
        self.btn_set_dir = ttk.Button(
            master=_PARENT[2],
            text="SET DIRECTORY",
            # command=self.fs_.ask_dir,
            command=self.get_directory,
            cnf=None,
        )
        self.btn_bulk_rename = ttk.Button(
            master=_PARENT[2],
            text="BULK RENAME",
            # command=self.p_.instructions,
            command=self.rename_files,
        )

        self.btn_set_dir.pack()
        self.btn_bulk_rename.pack()

    def raise_frame(self, frame):
        frame.tkraise()

    def get_directory(self):
        print("SET DIRECTORY Clicked...")
        # directory = self.fs_.ask_dir()
        return self.fs_.ask_dir()

    def rename_files(self):
        print("BULK RENAME Clicked...")
        if self.p_.instructions():
            print("Good Job!")
            image_dir = self.get_directory()
            timestamp = f"[{'%m'}{'%d'}_{'%H'}{'%M'}{'%f'}]"

            try:
                self.p_.create_temp_dir(
                    temp_dir := Path(
                        image_dir,
                        f"temp_{datetime.now().strftime(timestamp)}"
                    )
                )
                self.p_.copy_files(
                    self.p_.get_dir_list(image_dir),
                    temp_dir
                )
            except OSError as err:
                print(f"[ERROR] {err}")
            except TypeError as err:
                print(f"[ERROR] {err}")
            except Exception as err:
                print(f"[ERROR] {err}")
            # else:
            #     os.chdir(temp_dir)
            finally:
                # temp_dir_FULL = os.getcwd()
                temp_dir_FULL = Path(temp_dir).cwd()

            # dir_list_temp = os.listdir() \
                # if os.getcwd() == temp_dir_FULL else None
            dir_list_temp = Path(temp_dir).iterdir() \
                if Path.cwd() == temp_dir_FULL else None

            if dir_list_temp is not None:
                self.p_.rename_files(dir_list_temp)
        else:
            print("Proper naming convention required before running this utility!")


def main():
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


if __name__ == '__main__':
    main()
