# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
获取新日门店网的所有省市县区县信息
通过请求Ajax接口解析数据
'''

import pandas as pd

from Yadea.CompetitiveBrandStoreArea.utils.fileUtils import fileUtils
from Yadea.CompetitiveBrandStoreArea.utils.mysqlUtils import saveToMysql


def AiMaIngress():

    # 结果集数据
    resData = pd.read_csv('./Datas/AiMa/浙江.csv')
    print(resData)
    # 获取每个省的ajax路径
    proList = fileUtils().getCsvFile('D:\Maven\PyScrapy\Yadea\CompetitiveBrandStoreArea\Datas\AiMa\艾玛.csv')
    # 循环获取数据
    for index in range(0,31):
        list = []
        provinceName = str(proList[index][0])
        url = str(proList[index][1])
        print('爬取' + provinceName + ':' + url)
        # # 获取艾玛ajax接口数据
        # datas = requestsUtils().getUrl(url).replace('fwcallback(','').replace(')','')
        # # 转换json
        # jsonDatas = json.loads(datas)
        # # print(jsonDatas)
        # for item in jsonDatas:
        #     address = item['addr']
        #     # print(address)
        #     name = item['realname']
        #     # print(name)
        #     # 调用百度api获取经纬度
        #     lonlaturl = 'http://api.map.baidu.com/geocoding/v3/?address={0}&output=json&ak=K2WGZeDWlluoHpEpt5qo5Sx6VNyvffLB&callback=showLocation'.format(name)
        #     res = requestsUtils().getUrl(lonlaturl).replace('showLocation&&showLocation(','').replace(')','')
        #     # print(res)
        #     status = json.loads(res)['status']
        #     if status == 0:
        #         # 保存经纬度
        #         lon = json.loads(res)['result']['location']['lng']
        #         lat = json.loads(res)['result']['location']['lat']
        #         # 根据经纬度获取省市县
        #         pcd = praseUtils().lonlat2pcd(lon,lat)
        #         province = pcd[0]
        #         city = pcd[1]
        #         districd = pcd[2]
        #         town = pcd[3]
        #         street = pcd[4]
        #         resdict = {'province':province,'city':city,'districd':districd,'town':town,'street':street,'name':name,'lon':lon,'lat':lat,'address':address}
        #         print(resdict)
        #         list.append(resdict)
        # print(list)
        # # 保存csv格式
        # fileUtils().saveAsCsv(list,'AiMa/{}'.format(provinceName))

        # 合并数据集准备入库
        pdData = pd.read_csv('./Datas/AiMa/{0}.csv'.format(provinceName))
        # 取数据交集
        resData = pd.merge(resData , pdData, how='outer')

    print(resData)
    # pandans空字符串保存None
    resData = resData.astype(object).where(pd.notnull(resData), None)
    # 保存数据库
    saveToMysql(resData,'spider','storeareas_aima')

if __name__ == '__main__':
    AiMaIngress()