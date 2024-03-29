# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
获取新日门店网的所有省市县区县信息
通过请求Ajax接口解析数据
'''
import pandas as pd
from lxml import etree

from Yadea.CompetitiveBrandStoreArea.utils.fileUtils import fileUtils
from Yadea.CompetitiveBrandStoreArea.utils.mysqlUtils import saveToMysql
from Yadea.CompetitiveBrandStoreArea.utils.praseUtils import praseUtils


def XingRiIngress():

    # 结果集数据
    resData = pd.read_csv('./Datas/XingRi/西藏自治区.csv')
    print(resData)
    # 获取每个省的ajax路径
    proList = fileUtils().getCsvFile('D:\Maven\PyScrapy\Yadea\CompetitiveBrandStoreArea\Datas\XingRi\新日.csv')
    # 循环获取数据
    for index in range(0,32):
        provinceName = str(proList[index][0])
        ajaxPath = str(proList[index][1])

        # 读取ajax文件的数据
        data = fileUtils().getFileData(ajaxPath)
        # # 获取文件行数确定循环次数
        # line = data[0]/8
        # 保存数据的数组
        list = []
        # 数据转html
        xpath_data = etree.HTML(data[1])

        # 开始循环取店名
        for i in xpath_data.xpath('//dl'):
            # 店名称
            name = i.xpath('./dd/h3/text()')
            # 店地址
            address = i.xpath('./dd/p[1]/text()')
            # 经纬度
            lonlat = i.xpath('./@data-point')[0].split(',')
            lon = lonlat[1]
            lat = lonlat[0]
            # 访问百度地图接口，返回省市县
            pcd = praseUtils().lonlat2pcd(lat,lon)
            province = pcd[0]
            city = pcd[1]
            districd = pcd[2]
            town = pcd[3]
            street = pcd[4]
            list.append({'province':province,'city':city,'districd':districd,'town':town,'street':street,'name':name[0],'lon':lon,'lat':lat,'address':address[0]})
        print(provinceName + '=====>' + str(list))
        # 保存csv格式
        fileUtils().saveAsCsv(list,'XingRi/{}'.format(provinceName))

        # 合并数据集准备入库
        pdData = pd.read_csv('./Datas/XingRi/{0}.csv'.format(provinceName))
        # 取数据交集
        resData = pd.merge(resData , pdData, how='outer')

    print(resData)
    # pandans空字符串保存None
    resData = resData.astype(object).where(pd.notnull(resData), None)
    # 保存数据库
    saveToMysql(resData,'spider','storeareas_xingri')

if __name__ == '__main__':
    XingRiIngress()