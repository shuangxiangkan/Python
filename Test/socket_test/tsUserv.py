from socket import *
from time import ctime

HOST="localhost"
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)


udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("waiting for message...")
    data,addr=udpSerSock.recvfrom(BUFSIZ)
    Msg_sent=ctime()+data.decode()+" "
    udpSerSock.sendto(Msg_sent.encode(),addr)
    print("...received from and returned to:",addr)

udpSerSock.close()