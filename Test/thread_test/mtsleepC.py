import threading
import time

def test(p):
    time.sleep(0.1)
    print(p)

ts=[]

for i in range(15):
    th=threading.Thread(target=test,args=[i])
    ts.append(th)


for i in ts:
    i.start()
    # i.join()

for i in ts:
    i.join()

print("it is end!")