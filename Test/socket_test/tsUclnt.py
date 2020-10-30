from socket import *

HOST="10.10.64.182"
PROT=21567
BUFSIZ=1024
ADDR=(HOST,PROT)

udpCliSock=socket(AF_INET,SOCK_DGRAM)

while True:
    data=input("> ")
    if not data:
        break
    udpCliSock.sendto(data.encode(),ADDR)
    data,ADDR=udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode("utf-8"))

udpCliSock.close()

