from socket import *
import pickle
import threading
import time


HOST="localhost"
PORT=8888
BUFSIZE=2014
# ADDR=(HOST,PORT)
amount=2

# tcpCliSock = socket(AF_INET, SOCK_STREAM)
# tcpCliSock.connect(ADDR)

with open("hosts.txt", "r") as f:
    ips = f.readlines()

# for ip in ips:
#     print(ip)

def create_thread(number,amount,ADDR):
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    print("create_thread:",ADDR)
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

    # if number==1:
    #     while True:
    #         data = tcpCliSock.recv(BUFSIZE).decode("utf-8")
    #         if data == "results ready":
    #             print("最终结果为:")
    #             tcpCliSock.send("result_receive ready".encode("utf-8"))
    #             while True:
    #                 result=tcpCliSock.recv(BUFSIZE).decode("utf-8")
    #                 if result!="####":
    #                     print(result)
    #                 else:
    #                     break
    #             break

def main():

    # 开始时间
    start=time.time()

    number=1
    threads=[]
    for ip in ips:
        ADDR = (ip.strip(), PORT)
        print(ADDR)
        t=threading.Thread(target=create_thread,args=(number,amount,ADDR))
        threads.append(t)
        number+=1

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # tcpclientSock=

    end=time.time()
    print("总共耗时:",end-start)

main()