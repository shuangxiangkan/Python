import os
import time
import subprocess

subprocess.Popen(r'cmd')
print('打开成功')
time.sleep(5)
print('休息5s')
os.system(r'taskkill /F /IM 进程名')
print('关闭成功')
