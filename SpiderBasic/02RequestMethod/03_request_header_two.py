# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request


# 请求头
def load_baidu():
    url = "https://www.baidu.com"
    header = {
        # 浏览器版本,告诉浏览器我是真实的用户
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    # 创建请求对象
    request = urllib.request.Request(url, headers=header)
    # print(request)

    # 动态的添加请求头信息
    request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")

    # 获取请求头信息(打印所有头的信息)
    request_header = request.headers
    print(request_header)

    # 第二种方式打印headers信息
    print(request.get_header("User-agent"))

    # 获取完整的url
    print(request.get_full_url())

    # 请求网络数据(不在此处增加请求头，系统没有此参数)
    response = urllib.request.urlopen(request)
    print(response)
    data = response.read().decode("utf-8")
    with open("02header.html", "w", encoding="utf-8")as f:
        f.write(data)


load_baidu()
