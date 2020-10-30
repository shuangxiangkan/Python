from socket import *
from time import ctime


HOST="localhost"
PORT=21568
ADDRESS=(HOST,PORT)

server_socket=socket(AF_INET,SOCK_STREAM)
server_socket.bind(ADDRESS)
server_socket.listen(5)

BUFFERSIZE=1024
print("test")

while True:
    print("waiting for connection...")
    client_socket,addr=server_socket.accept()
    print("connection from:",addr)

    while True:
        data=client_socket.recv(BUFFERSIZE)
        if not data:
            break
        msg_send="["+ctime()+"]"+data.decode("utf-8")
        client_socket.send(msg_send.encode())

    client_socket.close()

server_socket.close()
