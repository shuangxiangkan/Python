import threading
from socket import *
from queue import Queue

q=Queue()


HOST="localhost"
PORT=8888
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(20)


def code_execute(number,amount,ip1):
    if int(number)==1:
        q.put(1)
        print(1)
        print(ip1)
    else:
        print("number",number)
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        print("first node:",ip1)
        ADDR=(ip1.strip(),PORT)
        while True:
            try:
                tcpCliSock.connect(ADDR)
            except:
                print("无法连接第一个节点")
            else:
                break


        # 发送"node"字符串，表明是计算节点发出的

        while True:
            tcpCliSock.send("node".encode("utf-8"))
            data=tcpCliSock.recv(BUFSIZ).decode("utf-8")
            if data=="node connect success":
                print(2)
                tcpCliSock.send(str(2).encode("utf-8"))
                break



def code_write_to_file(tcpCliSock):
    print("将代码写入文件")
    str = ""
    while True:
        # 将接收到的内容存到字符串str
        line = tcpCliSock.recv(BUFSIZ).decode("utf-8")
        if not line:
            break
        if line=="###":
            # 跳出内层循环
            break
        str += line

    print(str)
    # 将接收到的内容写入文件
    with open("compute.py", "w") as f:
        f.write(str)

def rece_code(tcpCliSock,addr):
    print("connection from",addr)
    tcpCliSock.send("control connect success".encode("utf-8"))
    number=tcpCliSock.recv(BUFSIZ).decode("utf-8")
    print("number:",number)
    amount = tcpCliSock.recv(BUFSIZ).decode("utf-8")
    print("amount:", amount)
    ip1= tcpCliSock.recv(BUFSIZ).decode("utf-8")
    print("first node.......",ip1)
    # 将代码写入文件
    code_write_to_file(tcpCliSock)
    code_execute(number,amount,ip1)


    # while True:
    #     print("queue的长度")
    #     if q.qsize() == 2:
    #
    #         print("queue中的所有元素为:")
    #         tcpCliSock.send("results ready".encode("utf-8"))
    #         data = tcpCliSock.recv(BUFSIZ).decode("utf-8")
    #         if data == "result_receive ready":
    #             while not q.empty():
    #                 r = q.get()
    #                 tcpCliSock.send(str(r).encode("utf-8"))
    #                 break
    #         tcpCliSock.send("####".encode("utf-8"))
    #         break


    # if int(number)==1:
    #     while True:
    #         tcpCliSock.send("results ready".encode("utf-8"))
    #         data=tcpCliSock.recv(BUFSIZ).decode("utf-8")
    #         if data=="result_receive ready":
    #             tcpCliSock.send(str(3).encode("utf-8"))
    #             break



def send_result(tcpCliSock,addr):
    print("connection from...", addr)
    tcpCliSock.send("node connect success".encode("utf-8"))
    data=tcpCliSock.recv(BUFSIZ).decode("utf-8")
    q.put(data)
    print(data)

def main():

    control_address=""
    while True:
        print("waiting for connection...")
        tcpCliSock, addr = tcpSerSock.accept()
        # 接收数据
        data = tcpCliSock.recv(BUFSIZ).decode("utf-8")
        # print(data)
        if data=="control":
            control_address=addr
            t=threading.Thread(target=rece_code,args=(tcpCliSock,addr))
            t.start()
            t.join()
        if data=="node":
            t=threading.Thread(target=send_result,args=(tcpCliSock,addr))
            t.start()
            t.join()


        # if q.qsize()==2:
        #
        #     print("queue中的所有元素为:")
        #     tcpCliSock.send("results ready".encode("utf-8"))
        #     data=tcpCliSock.recv(BUFSIZ).decode("utf-8")
        #     if data=="result_receive ready":
        #         while not q.empty():
        #             r=q.get()
        #             tcpCliSock.send(str(r).encode("utf-8"))
        #             break
        #     tcpCliSock.send("####".encode("utf-8"))


        if q.qsize()==2:

            print("queue中的所有元素为:")

            while not q.empty():
                r=q.get()
                print(r)


main()