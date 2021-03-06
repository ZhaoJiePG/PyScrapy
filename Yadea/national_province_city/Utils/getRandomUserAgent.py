# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import random


def getRandomUserAgent():
    user_agent_list = [{
                           'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"},
                       {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"},
                       {
                           'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
                       {'User-Agent': "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"},
                       {
                           'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201"}]
    # 每次请求的浏览器不一样
    random_user_agent = random.choice(seq=user_agent_list)

    return random_user_agent

