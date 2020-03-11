import tkinter as tk
import copy
import json
import math
import os

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)


class Menu(tk.Menu):
    def __init__(self, master)


class Application(tk.Tk):
    def __init__(self, master):
        super().__init__(master)
        self.geometry('{}x{}'.format(tk.Tk().winfo_screenwidth, tk.Tk().winfo_screenmmheight))
        self.main_frame = MainFrame(self.master).pack(fill = tk.BOTH, expand = 1)
        self.menu = Menu()
