# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import random

import requests
import time

user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
]
# 每次请求的浏览器不一样
random_user_agent = random.choice(user_agent_list)

# 代理IP
free_proxy={
    'http':'120.83.111.75:9999',
    'http':'112.85.129.166:9999',
    'http':'221.218.102.146:33323',
    'http':'120.83.111.19:9999',
    'http':'223.241.118.33:8010',
}

def getUrl(url):
    headers = {'User-Agent': random_user_agent}
    response = requests.get(url, headers=headers)
    response.encoding = 'GBK'
    data = response.text
    time.sleep(0.1)
    response.close()
    return data

def close(url):
    headers = {'User-Agent': random_user_agent}
    response = requests.get(url, headers=headers)
    response.encoding = 'GBK'
    data = response.text
    return data