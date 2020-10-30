import numpy as np
import matplotlib.pyplot as plt

# x=np.linspace(0,2*np.pi,10,endpoint=True)
# y1=np.sin(x)
# y2=np.cos(x)
# y3=np.tan(x)

x=['1 to 1','1 to 4','1 to 11']
y1=[328,340,591]
y2=[335,931,1395]
y3=[414,563,1079]


plt.plot(x,y1,color='r',linewidth=5,linestyle=':',label='data1')
plt.plot(x,y2,color='g',linewidth=2,linestyle="--",label='data2')
plt.plot(x,y3,color='b',linewidth=3,label='data3')
plt.legend(loc=2)

plt.title('line chart')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('figure1.pdf')
plt.show()