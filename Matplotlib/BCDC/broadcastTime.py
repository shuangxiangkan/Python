import numpy as np
import matplotlib.pyplot as plt
import os

# x=np.linspace(0,2*np.pi,10,endpoint=True)
# y1=np.sin(x)
# y2=np.cos(x)
# y3=np.tan(x)

x=['1 to 1','1 to 2','1 to 4','1 to 8','1 to 11','11 to 11']
y1=[328,359,440,457,591,787]
y2=[335,436,631,889,1395,4314]
y3=[404,414,563,866,1079,3738]


plt.plot(x,y1,marker='s',color='r',linewidth=2,linestyle=':',label='${A_3}$')
plt.plot(x,y2,marker='o',color='g',linewidth=2,linestyle="--",label='DCell$_{1,3}$')
plt.plot(x,y3,marker='v',color='b',linewidth=2,label='Fat-Tree')
plt.legend(loc=2)

# plt.title('line chart')
plt.xlabel('Different Types of Data Communication Algorithms')
plt.ylabel('Total Transmission Time(s)')

# for a,b in zip(x,y1):
#     plt.text(a,b,b,ha='center',va='bottom',color='r')
# for a,b in zip(x,y2):
#     plt.text(a,b,b,va='top',color='g')
# for a,b in zip(x,y3):
#     plt.text(a,b,b,ha='left',color='b')

dir='figure'
file='broadcastTime.jpg'
filePath=os.path.join(dir,file)
plt.savefig(filePath)
plt.show()