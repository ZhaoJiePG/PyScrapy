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
import datetime
import json
from time import sleep

import pandas as pd
import requests
from lxml import etree

from fileUtils import fileUtils
import os



# 高德接口url
def getGaoDeApi(keywords,cityQuery):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    # 保存数据list
    storeList=[]

    # 判断循环次数
    url = 'https://restapi.amap.com/v3/place/text?keywords={0}&key=59ed4a47216c3d36fef7397e8df1e903&city={1}&offset=20' \
        .format(keywords,cityQuery)
    response = requests.get(url).text
    # 获取总页数
    count = json.loads(response)['count']
    count = int(int(count)/20+2)
    # 开始循环
    for page in range(1,count):
        print('开始爬取：'+cityQuery+'-'+keywords+'-第'+str(page)+'页数据')
        # 高德接口url
        url = 'https://restapi.amap.com/v3/place/text?keywords={0}&key=59ed4a47216c3d36fef7397e8df1e903&city={1}&offset=20&page={2}'\
            .format(keywords,cityQuery,page)
        print(url)
        response = requests.get(url).text
        sleep(0.2)
        # 解析json
        datasList = json.loads(response)['pois']
        for items in datasList:
            name = items['name']
            address = items['address']
            if (address == []):
                address = ''
            lonlat = items['location'].split(',')
            lat = lonlat[0]
            lng = lonlat[1]
            tel = items["tel"]
            province = items['pname']
            city = items['cityname']
            area = items['adname']
            # 判断是否为空
            if (tel == [] ):
                tel="无"
            if (province == [] ):
                province="无"
            if (city == [] ):
                city="无"
            if (area == [] ):
                area="无"
            topic=keywords.replace('电动','')
            storeDict = {'add_time':now_time,'topic':topic,'name':name,'lat':lat,'lng':lng,'address':address,'province':province,'city':city,'area':area,'tel':tel}
            print(storeDict)
            storeList.append(storeDict)
    # 保存数据
    # print(storeList)
    fileUtils().saveAsCsv(storeList,'SingleInfo/{0}'.format(keywords+'_'+cityQuery))

# 合并csv文件
def mergeCsv():
    # 获取文件夹下的所有文件数
    fileList=''
    for dirs in os.walk('./Datas/StoreInfo'):
        fileList = dirs[2]
    resData = pd.read_csv('./Datas/dataFrame.csv')
    # 循环读数据
    for fileName in fileList:
        # 合并数据集
        csvFile='./Datas/StoreInfo/{0}'.format(fileName)
        print('开始合并'+str(csvFile)+'数据')
        pdData = pd.read_csv(csvFile,encoding='utf-8')
        # 取数据交集
        resData = pd.merge(resData , pdData, how='outer')

    resData = resData.astype(object).where(pd.notnull(resData), None)
    print(resData)
    # 保存文件
    fileUtils().saveAsCsv(resData,'AllStoreInfo')

    # # 保存数据库
    # saveToMysql(resData,'spider','storeareas_xingri')

# 腾讯接口url
def getTengXun(keywords,cityQuery):
    # 保存数据list
    storeList=[]

    # 判断循环次数
    url = 'https://restapi.amap.com/v3/place/text?keywords={0}&key=59ed4a47216c3d36fef7397e8df1e903&city={1}&offset=20' \
        .format(keywords,cityQuery)
    response = requests.get(url).text
    # 获取总页数
    count = json.loads(response)['count']
    count = int(int(count)/20+2)
    # 开始循环
    for page in range(1,count):
        print('开始爬取：'+cityQuery+'-'+keywords+'-第'+str(page)+'页数据')
        # 高德接口url
        url = 'https://restapi.amap.com/v3/place/text?keywords={0}&key=59ed4a47216c3d36fef7397e8df1e903&city={1}&offset=20&page={2}' \
            .format(keywords,cityQuery,page)
        print(url)
        response = requests.get(url).text
        sleep(0.2)
        # 解析json
        datasList = json.loads(response)['pois']
        for items in datasList:
            name = items['name']
            address = items['address']
            if (address == []):
                address = ''
            lonlat = items['location'].split(',')
            lat = lonlat[0]
            lng = lonlat[1]
            tel = items["tel"]
            province = items['pname']
            city = items['cityname']
            area = items['adname']
            # 判断是否为空
            if (tel == [] ):
                tel="无"
            if (province == [] ):
                province="无"
            if (city == [] ):
                city="无"
            if (area == [] ):
                area="无"
            topic=keywords.replace('电动','')
            storeDict = {'topic':keywords,'name':name,'lat':lat,'lng':lng,'address':address,'province':province,'city':city,'area':area,'tel':tel}
            print(storeDict)
            storeList.append(storeDict)
    # 保存数据
    # print(storeList)
    fileUtils().saveAsCsv(storeList,'SingleInfo/{0}'.format(keywords+'_'+cityQuery))


if __name__ == '__main__':
    storeQuery='金箭电动车'
    cityQuery='沭阳'
    getGaoDeApi(storeQuery,cityQuery)

