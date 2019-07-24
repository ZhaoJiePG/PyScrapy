# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
获取台铃光网门店数据：
http://www.tailg.com.cn/support#tailg_support
'''
import json
import os

import pandas as pd

from Yadea.CompetitiveBrandStoreArea.utils.fileUtils import fileUtils
from Yadea.CompetitiveBrandStoreArea.utils.praseUtils import praseUtils
from Yadea.CompetitiveBrandStoreArea.utils.requestsUtils import requestsUtils
from Yadea.CompetitiveBrandStoreArea.utils.mysqlUtils import saveToMysql

def TaiLinIngress():
    # 1.获取官网所有的省市编码id(ajax接口参数)
    url='http://www.tailg.com.cn/support#tailg_support'
    data = requestsUtils().getUrl(url)
    # 2.正则获取省市id 和省市名称
    regex="city_id = '(\d+)';city_name = '([\u4e00-\u9fa5]+)';"
    res1 = praseUtils().regex2str(regex,data)
    print(res1)
    for index in range(0,len(res1)):
        ajaxparam = res1[index][0]
        ajaxcity = res1[index][1]
        # 不请求省
        if(int(ajaxparam) >= 35):
            print('请求城市==='+ajaxcity)

        # 3.请求所有ajax接口,先获取总页数
        url2 = 'http://www.tailg.com.cn/information/ajaxsupportmapjs?cityid={0}&p={1}'.format(ajaxparam,1)
        data1 = requestsUtils().getUrl(url2)
        print(data1)
        data2 = json.loads(data1)

        # 4.判断总页数
        page_sum =data2['allpage']
        print('总共页数：'+ str(page_sum))
        # 判断是否有门店
        if(page_sum != 0):
            list = []

            # 5.循环页数,获取店名和位置
            for i in range(0,page_sum):
                data = json.loads(requestsUtils().getUrl('http://www.tailg.com.cn/information/ajaxsupportmapjs?cityid={0}&p={1}'.format(ajaxparam,i+1)))
                # print(data['areaAddressList'])
                for nameDict in data['areaAddressList']:
                    name = nameDict['salenet']
                    address = nameDict['detail']
                    print(name + '==' + address)
                    # 6.请求百度获取经纬度
                    lonlaturl = 'http://api.map.baidu.com/geocoding/v3/?address={0}&output=json&ak=K2WGZeDWlluoHpEpt5qo5Sx6VNyvffLB&callback=showLocation'.format(name)
                    res = requestsUtils().getUrl(lonlaturl).replace('showLocation&&showLocation(','').replace(')','')
                    # print(res)
                    # 7.请求百度获取省市县
                    status = json.loads(res)['status']
                    if status == 0:
                        # 保存经纬度
                        lon = json.loads(res)['result']['location']['lng']
                        lat = json.loads(res)['result']['location']['lat']
                        # 根据经纬度获取省市县
                        pcd = praseUtils().lonlat2pcd(lon,lat)
                        province = pcd[0]
                        city = pcd[1]
                        districd = pcd[2]
                        town = pcd[3]
                        street = pcd[4]
                        resdict = {'province':province,'city':city,'districd':districd,'town':town,'street':street,'name':name,'lon':lon,'lat':lat,'address':address}
                        print(resdict)
                        # 8.保存dict保存csv文件
                        list.append(resdict)
                        fileUtils().saveAsCsv(list,'TaiLin/{}'.format(ajaxcity))

def saveToMySql():
    # 结果集数据
    resData = pd.read_csv('./Datas/dfFormat.csv')
    # 9.pd读取datafram保存数据库
    allPath = fileUtils().eachFile('D:\Maven\PyScrapy\Yadea\CompetitiveBrandStoreArea\Datas\TaiLin')
    for path in allPath:
        csvPath = path.replace('TaiLin','TaiLin\\')
        print(csvPath)
        # 合并数据集准备入库
        pdData = pd.read_csv(csvPath)
        pdData = pdData.astype(object).where(pd.notnull(pdData), None)
        print(pdData)
        # 取数据交集
        resData = pd.merge(resData , pdData, how='outer')

    print(resData)
    # pandans空字符串保存None
    # resData = resData.astype(object).where(pd.notnull(resData), None)
    # 保存数据库
    saveToMysql(resData,'spider','storeareas_tailin')



if __name__ == '__main__':
    # 爬取数据
    # TaiLinIngress()
    # 保存数据入mysql
    saveToMySql()
