import numpy as np
import matplotlib.pyplot as plt
import os

x=['1 to 1','1 to 2','1 to 4','1 to 8','1 to 11','11 to 11']
y1=[25,39,44,59,67,89]
y2=[24,42,46,63,73,86]
y3=[27,48,49,65,75,92]


plt.plot(x,y1,marker='s',color='r',linewidth=2,linestyle=':',label='${A_3}$')
plt.plot(x,y2,marker='o',color='g',linewidth=2,linestyle="--",label='DCell$_{1,3}$')
plt.plot(x,y3,marker='v',color='b',linewidth=2,label='Fat-Tree')
plt.legend(loc=2)

# plt.title('line chart')
plt.xlabel('Different Types of Data Communication Algorithms')
plt.ylabel('Average CPU Usage Rate(%)')

dir='figure'
file='broadcastCpu.jpg'
filePath=os.path.join(dir,file)
plt.savefig(filePath)
plt.show()