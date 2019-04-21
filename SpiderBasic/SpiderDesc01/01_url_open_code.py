# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request


def load_data():
    url = "http://www.baidu.com/"
    # get的请求
    # http请求
    # http响应的对象
    response = urllib.request.urlopen(url)
    print(response)
    # 读取内容 bytes类型
    data = response.read()
    print(data)
    # 将获取的内容转换为字符串
    str_data = data.decode("utf-8")
    print(str_data)
    # 将数据写入文件
    with open("baidu.html", mode="w", encoding="utf-8")as f:
        f.write(str_data)
    # 将字符串类型转换为bytes
    str_name = "baidu"
    byte_name = str_name.encode("utf-8")
    print(byte_name)

    # python爬取的类型：str bytes
    # 如果爬取回来的是bytes类型：转换str类型decode("utf-8")
    # 如果爬取回来的是str类型：转换bytes类型decode("utf-8")

with open("baidu","w") as f:
    f.close()

load_data()
