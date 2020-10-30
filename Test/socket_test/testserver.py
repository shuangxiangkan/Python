from socket import *
from time import ctime

HOST="localhost"
PORT=12346
ADDR=(HOST,PORT)
BUFFERSIZE=1024

tcpser=socket(AF_INET,SOCK_STREAM)
tcpser.bind(ADDR)
tcpser.listen(5)
sum=0

while True:
    print("waiting for connection......")
    tcpclient,addr=tcpser.accept()
    print("connection from :",addr)

    while True:
        data=tcpclient.recv(BUFFERSIZE)
        if data.decode("utf-8")=="exit#":
            sendsum=str(sum)+"#"
            tcpclient.send(sendsum.encode("utf-8"))
            break
        print(data.decode("utf-8"))
        number=int(data.decode("utf-8").strip("#"))
        sum+=number

    tcpclient.close()
    sum=0

tcpser.close()

