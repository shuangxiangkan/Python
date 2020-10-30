import threading
from socket import *
from queue import Queue
import pickle

q=Queue()


HOST="localhost"
PORT=8888
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(20)


def code_execute(number,amount,tcpCliSock):
    dict={}
    dict["1:"]="a"
    dict["2:"]="b"

    tcpCliSock.send(pickle.dumps(dict))


def code_write_to_file(tcpCliSock):
    # print("将代码写入文件")
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
    # print("number:",number)
    amount = tcpCliSock.recv(BUFSIZ).decode("utf-8")
    # print("amount:", amount)
    ip1= tcpCliSock.recv(BUFSIZ).decode("utf-8")


    # 将代码写入文件
    code_write_to_file(tcpCliSock)

    code_execute(number,amount,tcpCliSock)
    # tcpCliSock.send("222222222".encode("utf-8"))
    # print("准备写入")





def main():
    while True:
        print("waiting for connection...")
        tcpCliSock, addr = tcpSerSock.accept()
        # 接收数据
        data = tcpCliSock.recv(BUFSIZ).decode("utf-8")
        if data=="control":
            t=threading.Thread(target=rece_code,args=(tcpCliSock,addr))
            t.start()
            t.join()



main()