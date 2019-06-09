# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 获取居委会代码函数---多线程实现
from queue import Queue
from threading import Thread

import time
from lxml import etree

from Yadea.national_province_city.Prases.urlUtils import getUrl


def getVillage(url_list):
    queue_village = Queue() #队列
    thread_num = 50 #进程数
    village = [] #记录街道信息的字典（全局）

    def produce_url(url_list):
        for url in url_list:
            queue_village.put(url) # 生成URL存入队列，等待其他线程提取

    def getData():
        while not queue_village.empty(): # 保证url遍历结束后能退出线程
            url = queue_village.get() # 从队列中获取URL
            data = getUrl(url)
            selector = etree.HTML(data)
            villageList = selector.xpath('//tr[@class="villagetr"]')
            #下面是爬取每个区的代码、URL
            for i in villageList:
                villageCode = i.xpath('td[1]/text()')
                UrbanRuralCode = i.xpath('td[2]/text()')
                villageName = i.xpath('td[3]/text()')
                #上面得到的是列表形式的，下面将其每一个用字典存储
                for j in range(len(villageCode)):
                    time.sleep(0.5)
                    village.append({'code':villageCode[j],'UrbanRuralCode':UrbanRuralCode[j],'name':villageName[j]})
                    print(str(villageName[j])+":"+str(villageCode[j]))

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
    return village