#!/bin/python

import tkinter as tk


class Split_Frame(tk.Frame):
    """A Frame which displays two frames alongside each other"""

    def __init__(self, master: tk.Frame):
        """Construct a new Split_Frame
        :param master: Parent frame, this frame is attached to.
        :type tk.Frame
        """
        tk.Frame.__init__(self, master=master)
        self.first = tk.Frame(self)
        self.second = tk.Frame(self)
        self.first.place(relx=0, y=0, relwidth=0.5, relheight=1)
        self.second.place(relx=0.5, y=0, relwidth=0.5, relheight=1)
