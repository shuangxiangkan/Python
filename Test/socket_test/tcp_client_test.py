from socket import *

HOST="10.10.66.46"
PORT=12345
ADDR=(HOST,PORT)

localhost="10.40.37.97"
localport=9000
localaddr=(localhost,localport)

BUFFERSIZE=1024

tcp_client_sock=socket(AF_INET,SOCK_STREAM)
tcp_client_sock.bind(localaddr)
tcp_client_sock.connect(ADDR)

while True:
    data = input(">")
    if not data:
        break
    tcp_client_sock.send(data.encode())
    data = tcp_client_sock.recv(BUFFERSIZE)
    if not data:
        break
    print(data.decode())

tcp_client_sock.close()
