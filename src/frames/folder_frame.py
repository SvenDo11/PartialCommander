#!/bin/python

import tkinter as tk


class Folder_Frame(tk.Frame):
    """A frame containing a folder view.
    :param master: The parent frame for this Folder_Frame.
    :type master: tk.Frame
    """

    def __init__(self, master: tk.Frame) -> None:
        super().__init__(master)
        self.vars = []
        for label in ["First", "Second", "Third"]:
            var = tk.StringVar(self, label)
            tk.Label(self, textvariable=var).pack()
            self.vars.append(var)
