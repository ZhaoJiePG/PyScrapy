# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from Yadea.national_province_city.Prases.urlUtils import getUrl
from lxml import etree

# 获取省级代码函数
def getProvince(url):
    province = []
    data = getUrl(url)
    selector = etree.HTML(data)
    provinceList = selector.xpath('//tr[@class="provincetr"]')
    for i in provinceList:
        provinceName = i.xpath('td/a/text()')

        print("爬取以下省信息\n "+str(provinceName))

        provinceLink = i.xpath('td/a/@href')
        for j in range(len(provinceLink)):
            provinceURL = url[:-10] + provinceLink[j]
            # key = str(provinceLink[j])[0:2]
            province.append({'name': provinceName[j], 'link': provinceURL})
            print(provinceName[j])
    return province
