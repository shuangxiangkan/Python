from socket import *
import pickle
import threading
import time


# HOST="localhost"
PORT=8888
BUFSIZE=2014
# ADDR=(HOST,PORT)

# tcpCliSock=socket(AF_INET,SOCK_STREAM)
# tcpCliSock.connect(ADDR)

# number:计算节点编号，从0开始
# amount:计算节点数目
# information={}
# information["number"]=-1
# information["amount"]=5


def send_code(ip,port,number,amount):

    global tcpCliSock

    information={}
    information["number"]=number
    information["amount"]=amount
    ADDR=(ip,port)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    # 发送"control"字符串，表明是控制节点发出的
    tcpCliSock.send("control".encode("utf-8"))

    tcpCliSock.send(pickle.dumps(information))
    data = tcpCliSock.recv(BUFSIZE)
    # if not data:
    #     break
    recv_date = data.decode("utf-8")
    if recv_date == "dict_success":
        tcpCliSock.send("code_ready".encode("utf-8"))
    with open("20185227018.py", "r") as f:
        lines = f.readlines()

    for line in lines:
        tcpCliSock.send(line.encode("utf-8"))

    tcpCliSock.send("###".encode("utf-8"))

    if number==0:
        while True:
            data=pickle.loads(tcpCliSock.recv(BUFSIZE))
            if data:
                print(data)
                break


    tcpCliSock.close()


def main():

    # 开始时间
    start=time.time()

    with open("hosts.txt", "r") as f:
        ips=f.readlines()

    # 计算节点个数
    amount=1
    # 计算节点编号，初始值为0
    number = 0

    threads = []

    for ip in ips:
        print(ip)
        t=threading.Thread(target=send_code,args=(ip,8888,number,amount))
        threads.append(t)
        # 计算节点编号+1
        number+=1

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    while True:
        data=tcpCliSock.recv(BUFSIZE)
        if data:
            print(pickle.loads(data))
            break


    # 结束时间
    end=time.time()

    print("一共用时:",(end-start))


main()



# class control_node(threading.Thread):
#     def __init__(self,information,HOST,PORT):
#         super().__init__()
#         self.information=information
#         self.ADDR=(HOST,PORT)
#         self.tcpCliSock = socket(AF_INET, SOCK_STREAM)
#         self.tcpCliSock.connect(ADDR)
#
#
#     def run(self):
#         print("发送节点编号和节点数量")
#         print("information", self.information)
#         self.tcpCliSock.send(pickle.dumps(self.information))
#         print("发送",pickle.dumps(self.information))
#         data = self.tcpCliSock.recv(BUFSIZE)
#         print("接收data")
#
#
#         recv_date = data.decode("utf-8")
#         print("recv_date",recv_date)
#         if recv_date == "dict_success":
#             print("接收字典成功")
#             self.tcpCliSock.send("code_ready".encode("utf-8"))
#         with open("20185227018.py", "r") as f:
#             lines = f.readlines()
#
#         for line in lines:
#             self.tcpCliSock.send(line.encode("utf-8"))
#
#         self.tcpCliSock.send("###".encode("utf-8"))
#
#         self.tcpCliSock.close()
#
#
# def main():
#     with open("hosts.txt","r") as f:
#         ips=f.readlines()
#
#     threads=[]
#     for ip in ips:
#         print(ip)
#         thread=control_node(information=information,HOST=ip,PORT=8888)
#         threads.append(thread)
#
#     for thread in threads:
#         thread.start()
#
#     for thread in threads:
#         thread.join()
#
#     print("控制节点结束")
#
# main()


# while True:
#     tcpCliSock.send(pickle.dumps(information))
#     data=tcpCliSock.recv(BUFSIZE)
#     if not data:
#         break
#     recv_date=data.decode("utf-8")
#     if recv_date=="dict_success":
#         tcpCliSock.send("code_ready".encode("utf-8"))
#     with open("20185227018.py","r") as f:
#         lines=f.readlines()
#
#     for line in lines:
#         tcpCliSock.send(line.encode("utf-8"))
#
#     tcpCliSock.send("###".encode("utf-8"))
#
#     while True:
#         pass
#
#
# tcpCliSock.close()