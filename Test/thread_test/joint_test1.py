import threading
import time

def test(p):
    time.sleep(0.001)
    print(p)

ts=[]

for i in range(15):
    th=threading.Thread(target=test,args=[i])
    ts.append(th)


for i in ts:
    i.start()

print("it is end!")