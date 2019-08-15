# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pandas as pd


class fileUtils():
    # 保存csv格式
    def saveAsCsv(self,data, name):
        df = pd.DataFrame(data).drop_duplicates()
        df.to_csv("./datas/{}.csv".format(name), sep=',', header=True, index=False, encoding='utf-8')
        print("{}.csv".format(name)+"保存成功")

    # 获取csv网址
    def getProMiYue(self,fileName):
        # 读取csv文件
        csv_file = open(fileName, 'rb').read().decode('utf-8')
        # 保存地区和url
        url_list = []
        for x in csv_file.split('\r\n'):
            url_info = x.split(',')
            url_list.append({url_info[0]:url_info[1]})

        return url_list