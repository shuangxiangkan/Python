import os
from time import sleep
from tkinter import *

class DirList(object):
    def __init__(self):
        self.top=Tk()
        self.label=Label(self.top,text='Directory Lister v1.1')
        self.label.pack()

        self.cwd=StringVar(self.top)
        print(self.cwd)

