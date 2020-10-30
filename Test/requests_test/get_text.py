import requests

# url="http://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png"
url="http://127.0.0.1:80/D/result.png"
path="D:/test.jpg"
r=requests.get(url,stream=True)
print(r.status_code)
with open(path,"wb") as f:
    f.write(r.content)