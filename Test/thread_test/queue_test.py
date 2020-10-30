from queue import Queue
from threading import Thread
import time
# maxsize默认为0，不受限
# 一旦>0,而消息数又达到限制，q.put()也将阻塞
# q=Queue(maxsize=0)

# 阻塞程序，等待队列消息
# q.get()

# 获取消息，等待队列消息
# q.get(timeout=0.5)

# 发送消息
# q.put()

# 等待所有的消息都被消费完
# q.join()

class Student(Thread):
    def __init__(self,name,queue):
        super().__init__()
        self.name=name
        self.queue=queue

    def run(self):
        while True:
            # 阻塞程序，时刻监听老师，接收消息
            msg=self.queue.get()
            # 一旦发现点到自己名字，就赶紧答道
            if msg==self.name:
                print("{}:到！".format(self.name))


class Teacher:
    def __init__(self,queue):
        self.queue=queue

    def call(self,student_name):
        print("老师:{}来了没？".format(student_name))
        #发送消息，要点谁的名
        self.queue.put(student_name)

queue=Queue()
teacher=Teacher(queue=queue)
s1=Student(name="小明",queue=queue)
s2=Student(name="小亮",queue=queue)
s1.start()
s2.start()

print("开始点名~")
teacher.call("小明")
time.sleep(1)
teacher.call("小亮")
