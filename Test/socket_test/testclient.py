from socket import *

HOST="localhost"
PORT=12345
ADDR=(HOST,PORT)
BUFFERSIZE=1024

testclient=socket(AF_INET,SOCK_STREAM)
testclient.connect(ADDR)


while True:
    data=input(">")
    if not data:
        break
    data+="#"
    testclient.send(data.encode())
    recdata=testclient.recv(BUFFERSIZE)
    if not recdata:
        break
    print(recdata.decode())

testclient.close()