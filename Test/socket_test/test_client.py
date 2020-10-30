import socket


HOST="10.10.64.182"
PORT=21568
ADDRESS=(HOST,PORT)


client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(ADDRESS)

BUFFERSIZE=1024

while True:
    data = input(">")
    if not data:
        break
    client_socket.send(data.encode())
    recv_data=client_socket.recv(BUFFERSIZE)
    if not recv_data:
        break
    print(recv_data.decode("utf-8"))

client_socket.close()