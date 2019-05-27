# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from threading import Thread

from lxml import etree
from queue import Queue

from Yadea.Prases.urlUtils import getUrl


def getCounty(url_list):
    queue_county = Queue() #队列
    thread_num = 10 #进程数
    county = [] #记录区级信息的字典（全局）

    def produce_url(url_list):
        for url in url_list:
            queue_county.put(url) # 生成URL存入队列，等待其他线程提取

    def getData():
        while not queue_county.empty(): # 保证url遍历结束后能退出线程
            url = queue_county.get() # 从队列中获取URL
            data = getUrl(url)
            selector = etree.HTML(data)
            countyList = selector.xpath('//tr[@class="countytr"]')
            #下面是爬取每个区的代码、URL
            for i in countyList:
                countyCode = i.xpath('td[1]/a/text()')
                countyLink = i.xpath('td[1]/a/@href')
                countyName = i.xpath('td[2]/a/text()')
                #上面得到的是列表形式的，下面将其每一个用字典存储
                for j in range(len(countyLink)):
                    countyURL = url[:-9] + countyLink[j]
                    county.append({'code':countyCode[j],'link':countyURL,'name':countyName[j]})
                    print(str(countyName[j]) +":"+str(countyCode[j]))
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
    return county