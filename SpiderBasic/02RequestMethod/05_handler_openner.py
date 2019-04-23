# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request

def handler_openner():
    # 系统的urlopen并没有添加代理功能，所以索要自定义
    # 安全套接层：第三方的CA数字证书
    # http80端口，https443端口
    # urlopen为什么可以请求数据：handler处理器，opener请求数据

    # urllib.request.urlopen()
    url = "https://www.cnblogs.com/zrmw/p/9332801.html"

    # 创建自己的处理器
    handler = urllib.request.HTTPHandler()

    # 创建自己的opener
    opener = urllib.request.build_opener(handler)

    # 用自己创建的opener来请求数据
    response = opener.open(url)
    data = response.read()
    print(response)
    print(data)

handler_openner()