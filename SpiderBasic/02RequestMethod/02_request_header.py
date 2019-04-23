# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request


# 请求头
def load_baidu():
    url = "http://www.baidu.com"

    # 创建请求对象
    request = urllib.request.Request(url)
    print(request)

    # 获取请求头信息
    request_header = request.headers
    print(request_header)

    # 请求网络数据
    response = urllib.request.urlopen(request)
    print(response)
    data = response.read().decode("utf-8")
    with open("02header.html","w",encoding="utf-8")as f:
        f.write(data)

    # 响应头
    # print(response.headers)


load_baidu()
