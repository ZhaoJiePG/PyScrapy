# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request

# 付费的代理发送
# 1.用户账号密码
# 通过验证的处理器来发送

def money_proxy_use():
    # 第一种方式付费
    # 1.代理IP
    money_proxy = {"http":"username:pwd@192.168.188.97"}

    # 2.代理的处理器
    proxy_handler = urllib.request.ProxyHandler(money_proxy)

    # 3.通过处理器创建opener
    opener = urllib.request.build_opener(proxy_handler)

    # 4.open发送请求
    opener.open("httpL..www.baidu.com")

    # 第二种方式发送IP
    user_name = "abcname"
    pwd = "123456"
    proxy_money = "123,12.31,4:8088"

    # 创建密码管理器，添加用户名密码
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm
    # url资源定位符
    password_manager.add_password(None,user_name,pwd)
    # 创建可以验证的ip处理器
    handler_proxy = urllib.request.ProxyBasicAuthHandler(password_manager)
    # 根据处理器创建opener
    opener_auth = urllib.request.build_opener(handler_proxy)
    # 发送请求
    response = opener_auth.open("http://www.baidu.com")
    print(response)

money_proxy_use()