# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
# pip install requests

url = 'http://www.baidu.com'
response = requests.get(url)

# contant属性：返回类型是bytes
data = response.content.decode("utf-8")

# text属性 文本字符串
data = response.text
print(type(data))