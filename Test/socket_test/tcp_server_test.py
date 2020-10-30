from socket import *
from time import ctime

HOST="10.10.64.182"
# HOST=socket.gethostname()
PORT=12345
ADDR=(HOST,PORT)
BUFFERSIZE=1024

tcp_server_sock=socket(AF_INET,SOCK_STREAM)
tcp_server_sock.bind(ADDR)
tcp_server_sock.listen(5)

while True:
    print("waiting to be connected...")
    tcp_client_sock, addr = tcp_server_sock.accept()
    print("connection from", addr)

    while True:
        data = tcp_client_sock.recv(BUFFERSIZE)
        if not data:
            break

        msg_send = "[" + ctime() + "] " + data.decode()
        tcp_client_sock.send(msg_send.encode())

    tcp_client_sock.close()

tcp_server_sock.close()