import json

# dic={"age":23,"job":"student"}
# dic_str=json.dumps(dic)
# print(type(dic_str),dic_str)
#
# dic_obj=json.loads(dic_str)
# print(type(dic_obj),dic_obj)

# dic={"age":23,"job":"student"}
# with open("abc.json","w",encoding="utf-8") as f:
#     json.dump(dic,f)

# with open("abc.json","r",encoding="utf-8") as f:
#     obj=json.load(f)
#     print(obj)


class Person:
    def __init__(self,name,age,job):
        self.name=name
        self.age=age
        self.job=job

    def work(self):
        print(self.name,"is working")


def person2dict(person):
    return {"name":person.name,
            "age":person.age,
            "job":person.job}


aa=Person("Bob",29,"Student")
print(aa.__dict__)
with open("abc.json","w",encoding="utf-8") as f:
    json.dump(aa,f,default=person2dict)

# dic={"age":23,"job":"student"}
# dic_str=json.dumps(dic)
# print(type(dic_str),dic_str)
#
# dic_obj=json.loads(dic_str)
# print(type(dic_obj),dic_obj)

# dic={"age":23,"job":"student"}
# with open("abc.json","w",encoding="utf-8") as f:
#     json.dump(dic,f)

# with open("abc.json","r",encoding="utf-8") as f:
#     obj=json.load(f)
#     print(obj)


class Person:
    def __init__(self,name,age,job):
        self.name=name
        self.age=age
        self.job=job

    def work(self):
        print(self.name,"is working")


def person2dict(person):
    return {"name":person.name,
            "age":person.age,
            "job":person.job}


aa=Person("Bob",29,"Student")
print(aa.__dict__)
with open("abc.json","w",encoding="utf-8") as f:
    json.dump(aa,f,default=person2dict)