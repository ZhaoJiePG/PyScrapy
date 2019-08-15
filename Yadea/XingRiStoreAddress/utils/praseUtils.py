# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class praseUtils():

    # 正则存数组
    def regex2arr(self,regexList):
        areaList = []
        dict = {}
        for index in range(0,len(regexList)):
            # 保存名称
            if(index % 6==0):
                name = ''
                for x in regexList[index]:
                    if x != '':
                        name = x
                dict.update({'name':name})
            # 保存经度
            if(index % 6==1):
                longitude=''
                for x in regexList[index]:
                    if x != '':
                        longitude = x[2:]
                dict.update({'longitude':longitude})
            # 保存纬度
            if(index % 6==2):
                latitude=''
                for x in regexList[index]:
                    if x != '':
                        latitude = x
                dict.update({'lon':latitude})
            # 保存地址
            if(index % 6==3):
                address=''
                for x in regexList[index]:
                    if x != '':
                        address = x
                dict.update({'address':address})
                # 清空字典
                dict = {}
            areaList.append(dict)
        return areaList
