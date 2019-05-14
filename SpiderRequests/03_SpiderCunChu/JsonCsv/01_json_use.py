# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# dict list - 字符串
import json

list = [{"name":"张三","age":20},{"name":"李四","age":18}]
data_json = json.dumps(list)
print(data_json)

# 文件对象 和dict list 转换
# with open('01json.json','w')as f:
#     f.write(data_json)
json.dump(list,open('01json.json','w'))

# 读取文件json -- list dict
fp = open('01json.json','r')
result = json.load(fp)
print(result)