from queue import Queue
import random
import threading
import time

class Producer(threading.Thread):
    def __init__(self,t_name,queue):# 传入线程名，实例化队列
        threading.Thread.__init__(self,name=t_name)
        self.data=queue

    def run(self):
        for i in range(5):# 生成0~4条队列
            print("%s: %s is producing %d to the queue!"%(time.ctime(),self.getName(),i))
            self.data.put(i) # 写入队列编号
            time.sleep(random.randrange(10)/5)
        print("%s:%s producing finished!"%(time.ctime(),self.getName())) #编号d队列完成操作

class Consumer(threading.Thread):

    def __init__(self,t_name,queue):
        threading.Thread.__init__(self,name=t_name)
        self.data=queue

    def run(self):
        for i in range(5):
            val=self.data.get()
            print("%s: %s is consuming. %d in the queue is consumed!"%(time.ctime(),self.getName(),val))
            time.sleep(random.randrange(10))

        print("%s: %s consuming finished"%(time.ctime(),self.getName()))

def main():
    queue=Queue()

    producer=Producer("Pro.",queue)
    consumer=Consumer("Con.",queue)
    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print("All threads terminate!")

if __name__=="__main__":
    main()
