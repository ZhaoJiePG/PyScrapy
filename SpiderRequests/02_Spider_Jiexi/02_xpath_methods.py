# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
import requests
from lxml import etree

url = 'http://news.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
res = requests.get(url=url,headers=headers)
data = res.content.decode("utf-8")

# 1.转接码类型
xpath_data = etree.HTML(data)

'''
xpath 语法：
    1.节点：/
    2.跨界点：//
    3.找精确的标签：//a[@属性="属性值"]
    4.标签包裹的内容：text()
    5.属性：@href
    6.平级可以用下标
    7.模糊查询[contaim(@class,"a")]
    8.下一个节点(平级关系)：folloing-sibling::*[index]
'''
# 2.调用xpath的方法
result = xpath_data.xpath('/html/head/title/text()')
result = xpath_data.xpath('//a/text()')
result = xpath_data.xpath('//a[@mon="c=civilnews&ct=0&a=27&col=8&locname=%E5%8D%97%E4%BA%AC&locid=2494"]/text()')
result = xpath_data.xpath('//a[@mon="ct=0&a=2&c=civilnews&pn=1"]/@href')
result1 = xpath_data.xpath('//li/a/text()')
result2 = xpath_data.xpath('//li/a/@href')
result2 = xpath_data.xpath('//div[contaim(@class,"a")]')
result_list = xpath_data.xpath('//div[contains(@class,"link-primary")]')
result_list = xpath_data.xpath('//head/following-sibling::*[1]')

print(len(result1))
print(len(result2))

res_dict = {result1[x]:result2[x] for x in range(0,len(result2))}

print(res_dict)