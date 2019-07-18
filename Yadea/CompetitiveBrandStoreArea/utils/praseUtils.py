# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import re

import requests



class praseUtils():

    # 正则解析
    def regex2str(self,regex,str):
        # res = re.findall(regex,str)
        pattern = re.compile(regex)
        res = pattern.findall(str)
        return res

    # 经纬度返回省市县
    def lonlat2pcd(self,lon,lat):
        url = 'http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location={0},{1}&output=json&pois=1&latest_admin=1&ak=K2WGZeDWlluoHpEpt5qo5Sx6VNyvffLB'
        response = requests.get(url.format(lat,lon))
        response.encoding = 'utf-8'
        data = response.text.replace('renderReverse&&renderReverse(','').replace(')','')
        baiDuDatas = json.loads(data)
        pcd=baiDuDatas['result']['addressComponent']
        province = pcd['province']
        city = pcd['city']
        districd = pcd['district']
        # res = self.regex2str(r'\"province\"\:\"([\u4e00-\u9fa5]+)\"\,\"city\"\:([\u4e00-\u9fa5]+)\,\"city_level\"\:2\,\"district\"\:([\u4e00-\u9fa5]+)',data)
        return [province,city,districd]

# data = praseUtils().lonlat2pcd('91.156633','29.656875')
# print(data)