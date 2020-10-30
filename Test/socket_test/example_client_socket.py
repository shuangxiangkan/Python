from socket import *
from time import ctime

HOST="localhost"
PORT=10001
ADDRESS=(HOST,PORT)

clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect(ADDRESS)

while True:
    data=input("请输入消息：")
    if not data:
        break

    clientSocket.send(data.encode("utf-8"))
    data=clientSocket.recv(1024)
    if not data:
        break

    print("服务器返回的消息是：",data.decode("utf-8"))

clientSocket.close()