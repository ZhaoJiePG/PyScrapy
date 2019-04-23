# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request

def create_proxy_handler():
    url = "https://www.cnblogs.com/zrmw/p/9332801.html"

    # 添加代理
    proxy = {
        # 免费的写法
        "http":"http://113.121.20.175:8080",
        "http":"http://60.2.44.182:9999",
        "http":"60.2.44.182:8080",

        # 付费的代理
        # "http":"xiaoming":123@192.169.0.0
    }

    # 代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 创建opener
    opener = urllib.request.build_opener(proxy_handler)

    # 拿代理IP发送请求
    data = opener.open(url).read()
    print(data)


create_proxy_handler()