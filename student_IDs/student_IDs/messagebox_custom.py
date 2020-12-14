#!/usr/bin/python3

# STANDARD LIBRARY IMPORTS
import tkinter as tk
from tkinter import (ttk, font as tk_font)
# THIRD PARTY IMPORTS

# LOCAL IMPORTS
from config import GUI_Setup


class MessageboxCustom:

    def __init__(self,
                 title: str,
                 msg_lbl: str,
                 geometry: str = "200x200",
                 ):
        self.toplevel_window = tk.Toplevel()
        self.toplevel_window.title(string=title)
        self.toplevel_window.geometry(newGeometry=geometry)
        self.toplevel_window['bg'] = GUI_Setup.COLORS['BLUE']['hex']
        self.msg_lbl = msg_lbl
        self.lbl_font = tk_font.Font(
            family=GUI_Setup.FONTS['MESSAGEBOX']['family'],
            size=GUI_Setup.FONTS['MESSAGEBOX']['size'],
            weight=GUI_Setup.FONTS['MESSAGEBOX']['weight'],
        )
        self.create_widgets()
        self.toplevel_window.mainloop()

    def create_widgets(self):
        self.label = ttk.Label(
            master=self.toplevel_window,
            text=self.msg_lbl,
            font=self.lbl_font,
        )
        self.button_confirm = ttk.Button(
            master=self.toplevel_window,
            text="CONFIRM",
            command=self.confirm,
        )
        self.button_cancel = ttk.Button(
            master=self.toplevel_window,
            text="CANCEL",
            command=self.cancel,
        )
        self.label.pack()
        self.button_confirm.pack()
        self.button_cancel.pack()

    def confirm(self):
        print("button.confirm clicked...")
        self.toplevel_window.destroy()
        return True

    def cancel(self):
        print("button.cancel clicked...")
        self.toplevel_window.destroy()
        return False
