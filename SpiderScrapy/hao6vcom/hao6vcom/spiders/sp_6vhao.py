# Author:Aliex ZJ
# @Time : 2020/12/1 15:22
# @File : sp_6vhao.py
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os,sys
sys.path.append('../../')
from SpiderScrapy.hao6vcom.hao6vcom.items import Hao6VcomItem
import scrapy


class Sp6vhaoSpider(scrapy.Spider):
    name = 'sp_6vhao'
    allowed_domains = ['hao6v.net']
    start_urls = ['http://www.hao6v.net/']

    def parse(self, response):
        films = []

        for s in response.xpath("//ul[@class='lt']/li"):

            item = Hao6VcomItem()

            fname = s.xpath("./a").extract()[0]
            links = s.xpath("./a/@href").extract()[0]

            item['fname'] = fname
            item['links'] = links


            films.append(item)

        print(films)

        return films
