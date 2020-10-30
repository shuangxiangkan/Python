from socket import *
from time import ctime


HOST="10.10.64.182"
PORT=12345
BUFFERSIZE=1024
ADDR=(HOST,PORT)

udp_server_sock=socket(AF_INET,SOCK_DGRAM)
udp_server_sock.bind(ADDR)


while True:
    print("waiting to be connected...")
    data,addr=udp_server_sock.recvfrom(BUFFERSIZE)
    Msg_send="["+ctime()+"] "+data.decode()
    udp_server_sock.sendto(Msg_send.encode(),addr)
    print("...received from and returned to:",addr)

udp_server_sock.close()
