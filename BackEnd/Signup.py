import requests

url = "http://localhost:5000/api/signup"

# 设置注册所需的用户名和密码
data = {"username": "admin", "password": "admin.12club"}

# 发送 POST 请求
response = requests.post(url, json=data)

# 检查响应状态码
if response.status_code == 201:
    print("Signup success")
else:
    print("Signup failed with status code:", response.status_code)
