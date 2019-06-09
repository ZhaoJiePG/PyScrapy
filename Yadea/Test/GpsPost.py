# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

str = 'date=1548376546000,1553675785000&ourSecretKey=outyadeaapi'

import hashlib

md = hashlib.md5()  # 构造一个md5
md.update(str.encode())
res = md.hexdigest()  # 加密后的字符串
print(res)

url = "http://test.vehicle.yadea.com.cn:9400/outDataApi/getBikeFault?date=1548376546000,1553675785000&yadeaKey="+res

import requests

response = requests.get(url=url)

print(response.status_code)

print(response.text)
