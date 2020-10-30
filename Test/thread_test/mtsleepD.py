import threading
from time import sleep,ctime

loops=[4,2]

class ThreadFunc(object):
    def __init__(self,func,args,name=""):
        self.name=name