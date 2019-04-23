# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request

def proxy_user():
    url = "https://www.cnblogs.com/zrmw/p/9332801.html"

    # 添加代理
    proxy_list = [
        {"http":"60.2.44.182:30963"},
        {"http":"119.102.28.205:9999"},
        {"http":"218.76.215.170:808"},
        {"http":"112.85.168.136:9999"},
        {"http":"111.177.181.125:9999"}
    ]
    for proxy in proxy_list:
        print(proxy)
        # 使用遍历出来的IP创建处理器
        procy_handler = urllib.request.ProxyHandler(proxy)
        # 创建opener
        opener = urllib.request.build_opener(procy_handler)
        opener.open(url)

        # 异常处理
        try:
            opener.open(url,timeout=1)
        except Exception as e:
            print(e)

proxy_user()