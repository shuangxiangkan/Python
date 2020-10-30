import time
from threading import Thread

class MyThread(Thread):
    def __init__(self,name="Python"):
        # 注意，super().__init__()一定要写
        # 而且要写在最前面，否则会报错
        super().__init__()
        self.name=name

    def run(self):
        for i in range(2):
            print("hello", self.name)
            time.sleep(1)


if __name__ == '__main__':
    # 创建线程01，不指定参数
    thread_01=MyThread()
    thread_01.start()
    # 创建线程，指定参数
    thread_02=MyThread("MING")
    thread_02.start()
