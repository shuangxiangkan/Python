import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self,func,args,name=""):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
        self.res=0

    def run(self):
        return self.res

    def getResult(self):
        print("starting",self.name,"at:",ctime())
        self.res=self.func(*self.args)
        print(self.name,"finished at:",ctime())

