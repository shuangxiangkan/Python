import matplotlib.pyplot as plt
import os
import numpy as np

bar_width = 0.2

x1 = np.arange(4)
x2=[i+bar_width for i in x1]
x3=[i+bar_width*2 for i in x1]
y1=[15.16,14.02,16.35,13.67]
y2=[14.70,13.71,14.84,10.72]
y3=[0,11.36,12.33,10.05]



tick_label = ['server failure','switch failure','link failure','hybrid failure']

plt.bar(x1, y1, bar_width, color="r", align="center", label="${A_3}$", alpha=0.5)
plt.bar(x2, y2, bar_width, color="b", align="center", label="DCell$_{1,3}$", alpha=0.5)
plt.bar(x3, y3, bar_width, color="g", align="center", label="Fat-Tree", alpha=0.5)

fontSize=7

for a,b in zip(x1,y1):
    plt.text(a,b,b,ha='center',va='bottom',color='r',fontsize=fontSize)
for a,b in zip(x2,y2):
    plt.text(a,b,b,ha='center',va='bottom',color='b',fontsize=fontSize)
for a,b in zip(x3,y3):
    plt.text(a,b,b,ha='center',va='bottom',color='g',fontsize=fontSize)

plt.xlabel("Four Types of Failures")
plt.ylabel(" Data Transfer Rate Per Second(m/s)")

plt.xticks(x1+bar_width/2, tick_label)

plt.legend()

dir='figure'
file='faultToleranceTransferRate.jpg'
filePath=os.path.join(dir,file)
plt.savefig(filePath)
plt.show()