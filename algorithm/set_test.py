# python中的set和其他语言类似，是一个无序不重复元素集，基本功能包括关系测试和消除重复元素
# x=set("spam")
# y=set(["h","a","m"])
# print(x,y)
# print(x&y)
# print(x|y)
# print(x-y)

# a=[11,22,33,44,11,22]
# b=set(a)
# print(b)
# c=[i for i in b]
# print(c)

t=set("Hello")# 创建一个唯一字符的集合
print(t)
t.add("x")
print(t)
t.remove("H")
print(t)
