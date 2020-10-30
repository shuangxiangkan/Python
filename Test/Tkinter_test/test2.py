import os
import time

# path="D:/test"
# ls = os.listdir(path)
# for i in ls:
#         c_path = os.path.join(path, i)
#         os.remove(c_path)




# print(ls)
# count = 0
# for i in ls:
#     if os.path.isfile(os.path.join(path,i)):
#         os.remove(i)
# print(count)

text=os.popen("test.exe")
time.sleep(3)
# os.system("taskkill /F /IM test.exe")

print(text)