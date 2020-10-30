import requests

response=requests.get("https://www.baidu.com")
print(type(response))
print(response.status_code)
print(type(response.text))

print(response.text)
response.encoding="utf-8"
print(response.text)


print(response.content)
print(response.content.decode("utf-8"))