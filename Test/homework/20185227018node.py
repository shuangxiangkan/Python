from socket import *
import threading
import pickle
import queue
import os

# HOST="10.10.64.182"
HOST="localhost"
PORT=8888
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

server_queue=queue.Queue()
results_queue=queue.Queue()



def rec_dict():
    # 当前计算节点标号，从0开始
    global number
    # 总计算节点个数
    global amount

    global tcpCliSock

    while True:
        print("waiting for connection...")
        tcpCliSock, addr = tcpSerSock.accept()
        # 接收数据
        data = tcpCliSock.recv(BUFSIZ).decode("utf-8")
        print("data",data)
        if not data:
            continue
        # 反序列化
        if data=="control":
            data = tcpCliSock.recv(BUFSIZ)
            dict_data = pickle.loads(data)
            print(dict_data)
            # 判断是否是字典类型，字典里面存放的是计算节点编号和计算节点数
            if isinstance(dict_data,dict):
                print("接收字典成功")
                number=dict_data["number"]
                amount=dict_data["amount"]
                # # 发送接收字典成功信号
                send_dic="dict_success"
                tcpCliSock.send(send_dic.encode("utf-8"))
                while True:
                    data=tcpCliSock.recv(BUFSIZ).decode("utf-8")
                    if data=="code_ready":
                        print("代码数据已经准备好")
                        # 将代码写入文件
                        code_write_to_file()
                        # 向队列中放入字典
                        server_queue.put(dict_data)

                        # 跳出内层循环
                        break

                # 跳出外层循环
                break


def code_write_to_file():
    print("将代码写入文件")
    str = ""
    while True:
        # 将接收到的内容存到字符串str
        line = tcpCliSock.recv(BUFSIZ).decode("utf-8")
        if not line:
            break
        if line=="###":
            # 跳出内层循环
            break
        str += line

    print(str)
    # 将接收到的内容写入文件
    with open("compute.py", "w") as f:
        f.write(str)



def code_execute():
    global result_one
    data=server_queue.get()
    # output1 = os.popen("python compute.py").readlines()
    # print(output1)

    # compute.all_prime(number,amount)
    if number!=0:
        # 发送"node"字符串，表明是控制节点发出的
        tcpCliSock.send("node".encode("utf-8"))

        tcpCliSock.send(number.encode("utf-8"))
    else:
        # result_one=[number]
        results_queue.put([number])



def watch():
    # global result_two
    flag=False

    amount=1

    result_two = []
    while True:
        i=0
        if i < (amount - 1):
            print("waiting for other computing nodes connected...")
            CliSock, addr = tcpSerSock.accept()
            print("connection form:",addr)
            data=CliSock.recv(BUFSIZ).decode("utf-8")

            if data=="node":
                data = CliSock.recv(BUFSIZ).decode("utf-8")
                result_two.append(data)
                CliSock.close()
                i+=1
            else:
                continue

        # if i==amount-2 and len(result_one)==1:
        if i == amount - 1 and not results_queue.empty():
            result_one=results_queue.get()
            results=result_one+result_two
            tcpSerSock.send(pickle.dumps(results))
            break


def main():
    threads = []
    t1=threading.Thread(target=rec_dict)
    t2=threading.Thread(target=code_execute)
    t3=threading.Thread(target=watch)
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

main()

# def main():
#     while True:
#         print("waiting for connection...")
#         global tcpCliSock
#         tcpCliSock, addr = tcpSerSock.accept()
#
#         if tcpCliSock:
#             print("... connected from:", addr)
#             threads=[]
#             t1=threading.Thread(target=rec_dict)
#             t2=threading.Thread(target=code_execute)
#             threads.append(t1)
#             threads.append(t2)
#
#             for thread in threads:
#                 thread.start()
#
#             for thread in threads:
#                 thread.join()
#
#             print("最终计算结果:",t2)
#
#             tcpCliSock.close()





