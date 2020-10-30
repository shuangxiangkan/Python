import threading
import time
import queue

class MyThread(threading.Thread):
    def __init__(self,func):
        super().__init__()
        self.func=func
    def run(self):
        self.func()

def worker():
    while not q.empty():
        item=q.get() # 获得任务
        print("Processing:",item)
        time.sleep(1)

def main():
    threads=[]
    for task in range(100):
        q.put(task)
    for i in range(threadNum):# 开启三个线程
        thread=MyThread(worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__=="__main__":
    q=queue.Queue()
    threadNum=3
    main()