# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

'''
json对象：js对象
json：ECMSCRIPT，ActionScript
json字符串：
'''

# JSON:轻量级数据交换格式
json_str = '{"name":"qiyue","age":18}'
# 解析json为dict类型
student = json.loads(json_str)
print(type(student))
print(student['age'])
print(student['name'])

json_str = [
    {"name": "qiyue", "age": 18, "flag": False},
    {"name": "qiyue1", "age": 20}
]
student = json.loads(json_str)
print(type(student))
print(type(student[0]))
print(student[1]['name'])
print(student[0]['name'])

# 序列化，字典转换为json
student = json.dump(json_str)


