import re

# m=re.match(r'^(\d{3})\-(\d{3,8})','010-12345')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))

# t='19:05:30'
# m=re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)
# print(m.groups())

# print(re.match(r'^(\d+?)(0*)$','102300').groups())

def is_vaild_email(addr):
    if re.match(r'^([a-zA-Z]|\.)+@[a-zA-Z]+.com$',addr):
        return True
    # elif re.match(r'[a-zA-Z]+@[a-zA-Z]+.com',addr):
    #    return True
# if is_vaild_email('someone@gmail.com'):
#     print("ok")
# else:
#     print("false")
assert is_vaild_email('someone@gmail.com')
assert is_vaild_email('bill.gates@microsoft.com')
assert not is_vaild_email('bob#example.com')
assert  not is_vaild_email('mr-bob@example.com')
print("ok")