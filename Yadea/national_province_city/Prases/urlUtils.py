# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import requests
import time

from Yadea.national_province_city.Utils.csvUtils import import_csv
from Yadea.national_province_city.Utils.getRandomUserAgent import getRandomUserAgent
from Yadea.national_province_city.Utils.getRandomIP import get_IP


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
    response.encoding = 'GBK'
    data = response.text
    time.sleep(0.1)
    response.close()
    return data


