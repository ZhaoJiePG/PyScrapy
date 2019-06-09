# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from lxml import etree
from Yadea.national_province_city.Prases.urlUtils import getUrl

# 获取市级代码函数
def getCity(url_list):
    city_all = []
    for url in url_list:
        data = getUrl(url)
        selector = etree.HTML(data)
        cityList = selector.xpath('//tr[@class="citytr"]')

        city = []
        for i in cityList:
            cityCode = i.xpath('td[1]/a/text()')
            cityLink = i.xpath('td[1]/a/@href')
            cityName = i.xpath('td[2]/a/text()')
            print("爬取："+str(cityName))
            for j in range(len(cityLink)):
                cityURL = url[:-7] + cityLink[j]
                city.append({'name': cityName[j], 'code': cityCode[j], 'link': cityURL})
                print(str(cityName[j]) + str(cityCode[j]))
        city_all.extend(city)
    return city_all

