#!/usr/bin/python3

# STANDARD LIBRARY IMPORTS
import tkinter as tk
from tkinter import (ttk, font as tk_font)
# THIRD PARTY IMPORTS

# LOCAL IMPORTS
from config import GUI_Setup, Button_Setup, Label_Setup, Messages


class MessageboxCustom:

    def __init__(self,
                 title: str,
                 msg_lbl: str,
                 geometry: str = "200x200",
                 ):
        self.toplevel_window = tk.Toplevel()
        self.toplevel_window.title(string=title)
        self.toplevel_window.geometry(newGeometry=geometry)
        self.toplevel_window['bg'] = GUI_Setup.COLORS['CORAL']['hex']
        self.msg_lbl = msg_lbl
        self.lbl_font = tk_font.Font(
            family=GUI_Setup.FONTS['MESSAGEBOX']['family'],
            size=GUI_Setup.FONTS['MESSAGEBOX']['size'],
            weight=GUI_Setup.FONTS['MESSAGEBOX']['weight'],
        )
        self.confirmed = None
        self.create_styles()
        self.create_widgets()
        self.toplevel_window.bind(
            "<Escape>",
            lambda e: self.destroy_window(self.toplevel_window)
        )
        self.toplevel_window.mainloop()

    def create_styles(self):
        self.ttk_style = ttk.Style()
        self.ttk_style.theme_use(themename="clam")
        self.ttk_style.configure(
            "MSG.TLabel",
            padding=(5,),
            background=GUI_Setup.COLORS['CORAL']['hex'],
            foreground=GUI_Setup.COLORS['WHITE']['hex'],
        )
        self.ttk_style.configure(
            "TButton",
            padding=(5,),
            relief="flat",
            background=GUI_Setup.COLORS['BLUE']['hex'],
            foreground=GUI_Setup.COLORS['WHITE']['hex'],
        )

    def create_widgets(self):
        self.label = ttk.Label(
            master=self.toplevel_window,
            text=self.msg_lbl,
            font=self.lbl_font,
            style="MSG.TLabel",
        )
        self.button_confirm = ttk.Button(
            master=self.toplevel_window,
            text="CONFIRM",
            style="TButton",
            command=self.confirm,
        )
        self.button_cancel = ttk.Button(
            master=self.toplevel_window,
            text="CANCEL",
            style="TButton",
            command=self.cancel,
        )
        # self.label.pack(side=tk.TOP)
        # self.button_confirm.pack(side=tk.LEFT, expand=True)
        # self.button_cancel.pack(side=tk.RIGHT, expand=True)
        self.label.grid({
            **Label_Setup.KWARGS_GRID_INIT,
            **Label_Setup.KWARGS_GRID_MSGBOX
        })
        self.button_confirm.grid({
            **Button_Setup.KWARGS_GRID_INIT,
            **Button_Setup.KWARGS_GRID_MSGBOX_CONF
        })
        self.button_cancel.grid({
            **Button_Setup.KWARGS_GRID_INIT,
            **Button_Setup.KWARGS_GRID_MSGBOX_CXL
        })

    def destroy_window(self, window):
        window.destroy()

    def confirm(self):
        print("button.confirm clicked...")
        self.destroy_window(self.toplevel_window)
        self.confirmed = True
        # return self.confirmed

    def cancel(self):
        print("button.cancel clicked...")
        self.destroy_window(self.toplevel_window)
        self.confirmed = False
        # return self.confirmed


def main():
    title = Messages.INSTRUCTIONS['title']
    msg_lbl = Messages.INSTRUCTIONS['message']
    geometry = "450x225"
    msgbox = MessageboxCustom(title=title, msg_lbl=msg_lbl, geometry=geometry)
    print(f"msgbox.confirmed: {msgbox.confirmed}")


if __name__ == '__main__':
    main()
