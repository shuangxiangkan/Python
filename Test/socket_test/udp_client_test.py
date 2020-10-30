from socket import *

HOST="10.10.64.182"
PORT=12345
BUFFERSIZE=1024
ADDR=(HOST,PORT)

udp_client_sock=socket(AF_INET,SOCK_DGRAM)

while True:
    data=input("> ")
    if not data:
        break
    udp_client_sock.sendto(data.encode(),ADDR)
    data,addr=udp_client_sock.recvfrom(BUFFERSIZE)
    if not data:
        break
    print(data.decode(),addr)

udp_client_sock.close()
