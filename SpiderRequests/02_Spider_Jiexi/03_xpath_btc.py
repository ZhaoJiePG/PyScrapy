# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import re

import os,sys
import requests
from lxml import etree

class BtcSpider(object):
    def __init__(self):
        self.base_url = 'https://www.chainnode.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }

    # 1.发送请求
    def get_response(self,url):
        response = requests.get(url, headers=self.headers)
        data = response.content.decode("utf-8")
        return data

    # 2.解析数据
    def parse_data(self,data):
        # 使用xpath解析页面所有的title和url
        # 路径：1.纯手写 2.借助浏览器 粘贴 路径
        xpath_data = etree.HTML(data)
        # 解析标题
        title_list = xpath_data.xpath('//a[@class="link-dark-major font-bold bbt-block"]/text()')
        # 解析网址
        url_list = xpath_data.xpath('//a[@class="link-dark-major font-bold bbt-block"]/@href')
        # 存入列表
        data_list = []
        for index,title in enumerate(title_list):
            news = {}
            news['names'] = title.replace(' ','').replace('\n','')
            news['url'] = 'https://www.chainnode.com'+url_list[index]
            data_list.append(news)

        # res_dict = {title_list[x]:'https://www.chainnode.com'+url_list[x] for x in range(0,len(url_list))}
        print(data_list)
        return str(data_list)

    # 3.保存数据
    def save_data(self,data):
        json_data = json.dumps(data)
        with open('btc.html','a',encoding="utf-8") as f:
            f.write(json_data+"\r\n")

    # 4.启动
    if(os.path.exists('btc.html')):
        os.remove("btc.html")
    def run(self):
        for i in range(1,5):
            # 1.拼接完整url
            url = self.base_url +'forum/61-'+str(i)
            print(url)

            # 2.发请求
            data = self.get_response(url)

            # 3.做解析
            result = url + ":   " +self.parse_data(data)

            # 4.保存

            self.save_data(result)

BtcSpider().run()

