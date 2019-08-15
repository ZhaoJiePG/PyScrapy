# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
百度获取地址信息
api.map.baidu.com/place/v2/search?query=台铃&region=海南省&output=json&ak=K2WGZeDWlluoHpEpt5qo5Sx6VNyvffLB
高德获取地址信息
https://restapi.amap.com/v3/place/text?keywords=台铃&key=cc59dda499458518a676fb0795bf235c&city=海南省
世界电动车网
http://www.qqddc.com/jxs.do?method=list&pb=40&pn=2
'''
import json
import requests
from lxml import etree

from fileUtils import fileUtils

# 高德接口url
def getTaiLinApi(keywords,city):
    print("爬取 "+city+"====="+keywords+" 门店信息")
    # 保存数据list
    storeList=[]
    for page in range (99,101):
        print('开始爬取：'+city+'-'+keywords+'-第'+str(page)+'页数据')
        # 百度接口url
        url = 'https://restapi.amap.com/v3/place/text?keywords={0}&key=cc59dda499458518a676fb0795bf235c&city={1}&offset=25&page={2}'\
            .format(city,keywords,page)
        # print(url)
        response = requests.get(url).text
        print(response)
        print(response['count'])
        if(response['count']==0):
            break
        # 解析json
        datasList = json.loads(response)['pois']
        for items in datasList:
            name = items['name']
            address = items['address']
            lonlat = items['location'].split(',')
            lat = lonlat[0]
            lng = lonlat[1]
            province = items['pname']
            city = items['cityname']
            area = items['adname']
            storeDict = {'name':name,'lat':lat,'lng':lng,'address':address,'province':province,'city':city,'area':area}
            print(storeDict)
            storeList.append(storeDict)

    print(storeList)

# 百度接口url
def getBaiDuApi(query,region,num):
    print("爬取 "+region+"====="+query+" 门店信息")
    # 保存数据list
    storeList=[]
    # 百度接口url
    url = 'http://api.map.baidu.com/place/v2/search?query={0}&region={1}&output=json&ak=K2WGZeDWlluoHpEpt5qo5Sx6VNyvffLB&page_size=20&page_num={2}'.format(query,region,num)
    response = requests.get(url).text
    # 解析json
    datasList = json.loads(response)
    results = datasList['results']
    for item in results:
        # 名称
        name = item['name']
        # 经纬度
        lat = item['location']['lat']
        lng = item['location']['lng']
        # 地址
        address = item['address']
        # 省市区县
        province = item['province']
        city = item['city']
        area = item['area']
        storeList.append({'name':name,'lat':lat,'lng':lng,'address':address,'province':province,'city':city,'area':area})
    print(storeList)
    fileUtils().saveAsCsv(storeList,'BaiDu_{0}_{1}_{2}'.format(region,query,num))

# 世界电动车
def getShiJieDianDongChe():
    url = 'http://www.qqddc.com/jxs.do?method=list&pb=40&pn=2'
    response = requests.get(url).text
    # 转换xpath
    xpathData = etree.HTML(response)
    a = xpathData.xpath('/html/body/div[3]/div[3]/div[3]/div[1]/ul/li[1]/div[2]/h1/a/text()')
    print(a)


if __name__ == '__main__':
    # getBaiDuApi('台铃','125',2)
    # getShiJieDianDongChe()
#琼山区、龙华区、秀英区、美兰区
    getTaiLinApi('海南省','台铃')