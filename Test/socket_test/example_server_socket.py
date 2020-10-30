from socket import *
from time import ctime


HOST="localhost"
PORT=10001
ADDRESS=(HOST,PORT)

serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(ADDRESS)
serverSocket.listen(5)

while True:
    print("等待客户端连接...")
    clientSocket,address=serverSocket.accept()
    print(address,"已经成功连接至本服务器")

    while True:
        data=clientSocket.recv(1024)
        if not data:
            break

        replyMsg=data.decode("utf-8")+"["+ctime()+"]"
        clientSocket.send(replyMsg.encode())

    clientSocket.close()

serverSocket.close()
