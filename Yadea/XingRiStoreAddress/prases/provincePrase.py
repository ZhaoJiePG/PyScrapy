# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from lxml import etree

# 获取省级代码函数
from Yadea.XingRiStoreAddress.utils.urlUtils import getUrl


def getProvince(url):
    province = []
    data = getUrl(url)

    selector = etree.HTML(data)
    provinceList = selector.xpath('//*[@id="province"]/option[2]/text')
    # for i in provinceList:
    #     provinceName = i.xpath('td/a/text()')
    #
    #     print("爬取以下省信息\n "+str(provinceName))
    #
    #     provinceLink = i.xpath('td/a/@href')
    #     for j in range(len(provinceLink)):
    #         provinceURL = url[:-10] + provinceLink[j]
    #         # key = str(provinceLink[j])[0:2]
    #         province.append({'name': provinceName[j], 'link': provinceURL})
    #         print(provinceName[j])
    return data

url='http://www.xinri.com/service/internet.html'
province = getProvince(url)
print(province)
