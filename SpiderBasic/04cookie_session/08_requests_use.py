# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json

import requests
# pip install requests

url = 'https://api.github.com/user'

# 这个网址返回的是json
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

response = requests.get(url,headers=headers)

data = response.content.decode("utf-8")

print(data)

# str--dict
data_dict = json.loads(data)
print(data_dict)

data = response.json()
print(data)