# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request

def auth_nei_wang():
    # 1.用户名密码
    user = "admin"
    pwd = "admin123"
    nei_url = "http://10.149.1.154"

    # 2.创建密码管理器
    pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    pwd_manager.add_password(user=user,passwd=pwd)
    # 创建可以验证的ip处理器
    handler_proxy = urllib.request.ProxyBasicAuthHandler(pwd_manager)
    # 根据处理器创建opener
    opener_auth = urllib.request.build_opener(handler_proxy)
    # 发送请求
    response = opener_auth.open("http://www.baidu.com")
    print(response)
