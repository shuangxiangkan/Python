# # from threading import Lock,Thread
# import time
#
#
# # lock=Lock()
# # g=0
#
# def add_one(lock,g):
#     global g
#     while True:
#         lock.acquire()
#         g+=1
#         # time.sleep(1)
#         print("thread-1",g)
#         lock.release()
#         # print("thread-1 release")
#         time.sleep(1)
#
# def add_two(lock,g):
#     global g
#     while True:
#         lock.acquire()
#         g+=2
#
#         print("thread-2", g)
#         lock.release()
#         time.sleep(1)
#
# # threads=[]
# # for func in [add_one,add_two]:
# #     threads.append(Thread(target=func))
# #     threads[-1].start()
#
