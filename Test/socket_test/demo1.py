import socket

def send_msg(udp_socket):
    msg=input("请输入你要发送的内容：")
    ip="192.168.72.1"
    port=8080
    udp_socket.sendto(msg.encode("utf-8"),(ip,port))


def recv_msg(udp_socket):
    recv_data=udp_socket.recvfrom(1024)
    ip=recv_data[1]
    msg=recv_data[0].decode("gbk")
    print(">>>%s：%s"%(str(ip),(msg)))


def main():
    # 创建
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(("",8081))
    while True:
        print("-"*20)
        print("1.发送消息")
        print("2.接收消息")
        print("-" * 20)
        op_num = input("请输入你要选择的功能序号：")
        if op_num=="1":
            send_msg(udp_socket)
        elif op_num=="2":
            recv_msg(udp_socket)
        else:
            print("输入有误，请重新输入")


if __name__ == '__main__':
    main()