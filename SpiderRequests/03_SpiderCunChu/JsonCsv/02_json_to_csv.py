# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import csv

# 需求 json 中的数据 转换成 csv文件

# 1.分别 读，创建文件
json_fp = open('01json.json','r')
csv_fp = open('02csv.csv','w')

# 2.提出 表头，表内容
data_list = json.load(json_fp)

# sheet_title = data_list[0].keys()
sheet_title = {"姓名","年龄"}

sheet_data = []
for data in data_list:
    sheet_data.append(data.values())

# 3.csv写入器
writer = csv.writer(csv_fp)

# 4.写入表头
writer.writerow(sheet_title)

# 5.写入表内容
writer.writerows(sheet_data)

# 6.关闭文件流
json_fp.close()
csv_fp.close()
