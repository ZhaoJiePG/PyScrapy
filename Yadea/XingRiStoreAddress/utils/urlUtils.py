# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import requests

from Yadea.XingRiStoreAddress.utils.UserAgents import getRandomUserAgent


def getUrl(url):
    # 获取随机请求头
    headers = getRandomUserAgent()

    # getip = get_IP()
    #
    # random_ip = getip.get_random_ip
    # # 获取随机代理ip
    # proxies = {"http": random_ip}
    # print(proxies)

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    data = response.text
    time.sleep(0.1)
    response.close()
    return data