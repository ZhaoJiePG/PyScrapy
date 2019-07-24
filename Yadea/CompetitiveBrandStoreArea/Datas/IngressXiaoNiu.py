# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
获取小牛关网门店数据：
https://www.niu.com/service/expstore?type=1
小牛全国地图url
https://www.niu.com/api/offline-store/searchStoreByDistance/30.221735/116.101829/5186/B,C,D,F,G
'''
import json

import pandas as pd

from Yadea.CompetitiveBrandStoreArea.utils.fileUtils import fileUtils
from Yadea.CompetitiveBrandStoreArea.utils.mysqlUtils import saveToMysql
from Yadea.CompetitiveBrandStoreArea.utils.praseUtils import praseUtils
from Yadea.CompetitiveBrandStoreArea.utils.requestsUtils import requestsUtils

# 1.请求小牛的全国门店url
url = 'https://www.niu.com/api/offline-store/searchStoreByDistance/30.221735/116.101829/5186/B,C,D,F,G'
# url = 'https://www.niu.com/api/offline-store/searchStoreByDistance/31.57916/120.49636/53/B,C,D,F,G'
datas = requestsUtils().getUrl(url)
jsonDatas = json.loads(datas)
# 2.获取门店信息
dictDatas = jsonDatas['items']
dataList = []
# 3.循环解析信息
for item in dictDatas:
    # print(item)
    name = item['name']
    address = item['address']
    lat = item['lat']
    lon = item['lng']
    # 4.根据经纬度获取省市县
    pcd = praseUtils().lonlat2pcd(lon,lat)
    province = pcd[0]
    city = pcd[1]
    districd = pcd[2]
    town = pcd[3]
    street = pcd[4]
    # 5.保存数据字典
    resdict = {'province':province,'city':city,'districd':districd,'town':town,'street':street,'name':name,'lon':lon,'lat':lat,'address':address}
    print(resdict)
    dataList.append(resdict)


# 6.保存csv文件
df = pd.DataFrame(dataList)
df.to_csv("D:\Maven\PyScrapy\Yadea\CompetitiveBrandStoreArea\Datas\XiaoNiu\store.csv", sep=',', header=True, index=False, encoding='utf-8')

# fileUtils().saveAsCsv(dataList,'store')

# 7.存储mysql
# pandans空字符串保存None
resData = pd.read_csv('D:\Maven\PyScrapy\Yadea\CompetitiveBrandStoreArea\Datas\XiaoNiu\store.csv')
resData = resData.astype(object).where(pd.notnull(resData), None)
print(resData)
# 保存数据库
saveToMysql(resData,'spider','storeareas_xiaoniu')