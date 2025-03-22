#!/bin/python

import tkinter as tk
from frames.split_frame import Split_Frame
from frames.folder_frame import Folder_Frame


class Main_Window(tk.Tk):
    """A Window containing a menu and content in the following layout:
    |-------------------------------------|
    |                 Menu                |
    |-------------------------------------|
    |                                     |
    |              Content                |
    |                                     |
    |-------------------------------------|
    """

    def __init__(self, menu_height: int = 100) -> None:
        """Construct a new Main_Window.
        :param menu_height: Height of the menu in px, default to 100
        :type menu_height: int
        """
        tk.Tk.__init__(self)
        self.menu_frame = tk.Frame(self, background="red", height=menu_height)
        self.content_frame = tk.Frame(self, background="yellow")
        self.menu_frame.place(x=0, y=0, relwidth=1, height=menu_height)
        self.content_frame.place(x=0, y=menu_height, relwidth=1, relheight=0.8)
        # self.menu_frame.pack(side=tk.TOP, fill=tk.X, expand=True)
        # self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.setupContent()

    def setupContent(self) -> None:
        """Setup the Content frame"""
        self.split_frame = Split_Frame(self.content_frame)
        self.split_frame.pack(expand=True, fill=tk.BOTH)
        Folder_Frame(self.split_frame.first).pack(padx=5, pady=5)
        Folder_Frame(self.split_frame.second).pack(padx=5, pady=5)


if __name__ == "__main__":
    root = Main_Window()
    root.mainloop()
