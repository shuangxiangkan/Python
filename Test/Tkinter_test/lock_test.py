# from threading import Lock,Thread
# from prodcons import add_one,add_two
#
# lock=Lock()
# g=0
#
# def test_one(lock,g):
#     global g
#     add_one(lock,g)
#
# def test_two(lock,g):
#     global g
#     add_two(lock,g)
#
#
# threads=[]
# threads.append(Thread(target=test_one,args=(lock,g)))
# threads.append(Thread(target=test_two,args=(lock,g)))
#
# for i in threads:
#     i.start()