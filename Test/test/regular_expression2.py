import re

def name_of_email(addr):
    first=re.compile(r'^\<([a-zA-Z|\s]+)\>[a-zA-Z]+@[a-zA-Z]+.org$')
    second=re.compile(r'^([a-zA-Z]+)@[a-zA-Z]+.org$')
    #name=re.match(r'^\<([a-zA-Z|\s]+)\>[a-zA-Z]+@[a-zA-Z]+.org$',addr)
    name=None
    if first.match(addr):
        name=first.match(addr)
        print(name.groups())
    elif second.match(addr):
        name=second.match(addr)
        print(name.groups())
    return name.group(1)


print(name_of_email('<Tom Paris>tom@voyager.org'))
print(name_of_email('tom@voyager.org'))