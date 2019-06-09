# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 获取街道代码函数---多线程实现
from threading import Thread

import time
from lxml import etree
from queue import Queue

from Yadea.national_province_city.Prases.urlUtils import getUrl


def getTown(url_list):
    queue_town = Queue() #队列
    thread_num = 20 #进程数
    town = [] #记录街道信息的字典（全局）

    def produce_url(url_list):
        for url in url_list:
            queue_town.put(url) # 生成URL存入队列，等待其他线程提取

    def getData():
        while not queue_town.empty(): # 保证url遍历结束后能退出线程
            url = queue_town.get() # 从队列中获取URL
            data = getUrl(url)
            selector = etree.HTML(data)
            townList = selector.xpath('//tr[@class="towntr"]')
            #下面是爬取每个区的代码、URL
            for i in townList:
                townCode = i.xpath('td[1]/a/text()')
                townLink = i.xpath('td[1]/a/@href')
                townName = i.xpath('td[2]/a/text()')
                #上面得到的是列表形式的，下面将其每一个用字典存储
                for j in range(len(townLink)):
                    # 中山市、东莞市的处理
                    if url == 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/44/4419.html' or url == 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/44/4420.html':
                        townURL = url[:-9] + townLink[j]
                    else:
                        townURL = url[:-11] + townLink[j]
                    print(str(townName[j])+":"+str(townCode[j]))
                    time.sleep(0.1)
                    town.append({'code':townCode[j],'link':townURL,'name':townName[j]})


    def run(url_list):
        produce_url(url_list)

        ths = []
        for _ in range(thread_num):
            th = Thread(target = getData)
            th.start()
            ths.append(th)
        for th in ths:
            th.join()

    run(url_list)
    return town