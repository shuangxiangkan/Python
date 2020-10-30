from collections import deque


graph={}
graph["you"]=["bob","claire","alice"]
graph["bob"]=["anuj","peggy"]
graph["claire"]=["thom","jonny"]
graph["alice"]=["peggy"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"]=[]
graph["jonny"]=[]

def judge(current_element):
    if current_element[-1]=="m":
        return True
    else:
        return False

def my_breadth_first_search(name):
    queue=deque()
    searched = []
    queue+=graph[name]
    while queue:
        current_element = queue.popleft()
        if current_element not in searched:
            if judge(current_element):
                print("The mango seller is:"+current_element)
                return True
            else:
                searched.append(current_element)
                queue+=graph[current_element]


my_breadth_first_search("you")
