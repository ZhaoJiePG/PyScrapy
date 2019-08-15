# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import time

import requests

from Yadea.CompetitiveBrandStoreArea.utils.stringUtils import stringUtils


class requestsUtils():

    # 获取随机请求头
    def getRandomAgent(self):
        user_agent_list = [
            {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"},
            {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"},
            {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400"}]
        # 每次请求的浏览器不一样
        random_user_agent = random.choice(seq=user_agent_list)

        return random_user_agent

    # 获取请求信息
    def getUrl(self,url):
        # 获取随机请求头
        headers = self.getRandomAgent()
        response = requests.get(url, headers=headers)
        data = response.text
        time.sleep(0.1)
        response.close()
        return data

# print(requestsUtils().getAjaxDatas('http://www.xinri.com/Ajax/AjaxHandler_XRDDC.ashx'))



