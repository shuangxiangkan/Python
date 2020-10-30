from socket import *

# The HOST and PORT variables refer to the server's hostname and port number
HOST="10.10.64.182"
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data=input("> ")
    if not data:
        break
    tcpCliSock.send(data.encode())
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode())

tcpCliSock.close()