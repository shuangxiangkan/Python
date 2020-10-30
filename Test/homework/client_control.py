from socket import *
import pickle
import threading
import time
from queue import Queue


# HOST="localhost"
PORT=8888
BUFSIZE=2014
# ADDR=(HOST,PORT)
amount=2

q=Queue()

with open("hosts.txt", "r") as f:
    ips = f.readlines()



def create_thread(number,amount,ADDR):
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    # 发送"control"字符串，表明是控制节点发出的
    tcpCliSock.send("control".encode("utf-8"))
    flag=tcpCliSock.recv(BUFSIZE).decode("utf-8")
    if flag=="control connect success":
        # 计算节点编号
        # number=1
        tcpCliSock.send(str(number).encode("utf-8"))
        # number+=1
        # 计算节点总个数
        # amount=5
        tcpCliSock.send(str(amount).encode("utf-8"))
        # 发送第一个节点的ip地址
        tcpCliSock.send(str(ips[0]).encode("utf-8"))


        with open("20185227018.py", "r") as f:
            lines = f.readlines()

        for line in lines:
            tcpCliSock.send(line.encode("utf-8"))

        tcpCliSock.send("###".encode("utf-8"))

        # while True:
        #     data = tcpCliSock.recv(BUFSIZE).decode("utf-8")
        #     if not data:
        #         print(data)
        #         break
        data = tcpCliSock.recv(BUFSIZE)
        data=pickle.loads(data)
        results=[]
        for i in data.keys():
            results.append(data[i])
        # print(data)
        q.put(results)



        # while True:
        #     print("是否执行1")
        #     data=tcpCliSock.recv(BUFSIZE).decode("utf-8")
        #     if data=="results_ready":
        #         tcpCliSock.send("ready too".encode("utf-8"))
        #         result=tcpCliSock.recv(BUFSIZE).decode("utf-8")
        #         print("是否执行2")
        #         if not result:
        #             print(result)
        #             break
        #         else:
        #             print("没有得到数据")




def main():

    # 开始时间
    start=time.time()

    number=1
    threads=[]
    for ip in ips:
        ADDR = (ip.strip(), PORT)
        t=threading.Thread(target=create_thread,args=(number,amount,ADDR))
        threads.append(t)
        number+=1

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


    print("最终结果为：")
    while not q.empty():
        print(q.get())


    end=time.time()
    print("总共耗时:",end-start)

main()