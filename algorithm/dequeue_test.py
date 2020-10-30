from collections import deque

# 实例化一个deque对象
# d=deque()

# 和list的对象有些类型
# d.append("a")
# d.append("b")
# d.append("c")
# print(len(d))
# print(d[0])
# print(d[-1])
# print(d)

# 从队列的两段pop数据
#
# d1=deque("abcd")
# print(d1)
# d1.popleft()
# print(d1)
# d1.pop()
# print(d1)

# d=deque(maxlen=5)# 限制元素为5
#
# d.append(1)
# d.append(2)
# d.append(3)
# d.append(4)
# d.append(5)
# print(d)
# d.append(6)
# d.append(7)
# print(d)

d=deque([1,2,3,4,5])
print(d)
d+=[6,7]
# d.append([6,7])
element=d.popleft()
print(d)
print(element)
print(d)
