from socket import *
import math

HOST="10.40.34.8"
PORT=5000
ADDR=(HOST,PORT)
BUFFERSIZE=1024

client_sock=socket(AF_INET,SOCK_STREAM)
client_sock.connect(ADDR)

flag=True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

while True:
    data = input(">")
    data += "#"
    client_sock.send(data.encode("utf-8"))
    print("send:",data)
    recv_data=client_sock.recv(BUFFERSIZE)
    print("rec:",recv_data.decode("utf-8"))
    if recv_data.decode("utf-8")!="ACK#":
        break
    number_byte=client_sock.recv(BUFFERSIZE)
    print("rec:",number_byte.decode("utf-8"))
    number=int(number_byte.decode("utf-8").strip("#"))

    if is_prime(number):
        data="TRUE#"
    else:
        data="FALSE#"

    client_sock.send(data.encode("utf-8"))
    print("send:",data)
    rec_flag=(client_sock.recv(BUFFERSIZE)).decode("utf-8")
    print("rec:",rec_flag)

    break

client_sock.close()



