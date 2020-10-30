import socket

# 创建udp的套接字
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 实现功能，udp网络程序 发送数据
# 1.准备接收方的地址
address=("192.168.72.1",8080)# 元组数据类型
# 2.从键盘获取数据
send_data=input("请输入要发送的内容:")
# 3.发送数据
udp_socket.sendto(send_data.encode("gbk"),address)
# 4.接收对方发送过来的数据
recv_date=udp_socket.recvfrom(1024)
# 5.显示对方发送的数据
# 接收到的数据是一个元组类型的数据
# 第一个元素是对方发送的数据
# 第二个元素是对方的地址(ip和端口号)
print(recv_date[0].decode("gbk"))

# 关闭套接字
udp_socket.close()