# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from lxml import etree

import requests
import re

# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

# session模拟用户登陆=cookiejar
session = requests.session()

# 模拟的登陆页面
post_url = "http://www.chinaccm.cn/MemberCenter/Login.aspx"

# post请求保存的账号密码
post_data = {"txtUserName": "yadea雅迪科技", "txtPassWord": "yadea001"}

# 模拟登陆
responsee = session.post(url=post_url, data=post_data, headers=headers)
# print(responsee.content.decode())

# 二次请求的网址
url = 'http://www.chinaccm.cn/pricedata/PriceData.aspx?Type=DATA_NATIONALPRICE%2c国内价格&Cata=1&scode=350204&limit=Grade%2cADC12%3bLocalityName%2c上海%3b&cdtion=&dshow=Date%2cSuppName%2cSpec%2cSpecModelName%2cGrade%2cPrice%2cPriceXXChange%2cBottomPrice%2cHighPrice%2cAvgPrice%2cAvgPriceXXChange%2cProvinceName%2cPriceTell%2cPriceUnit%2cMarketName%2cAreaName%2cCityName%2cPortName%2cLocalityName%2cContract%2cPlaceOfDelivery%2cMarks%2cMainPrice'

# session接受调用cookie
response = session.get(url=url, headers=headers)
context = response.text

# 解析
selector = etree.HTML(context)
table = []

date = selector.xpath('//tr[@class="dmain_right_tab_list"][1]/td[1]/text()')
name = selector.xpath('//tr[@class="dmain_right_tab_list"][1]/td[2]/text()')
num = selector.xpath('//tr[@class="dmain_right_tab_list"][1]/td[3]/text()')
price = selector.xpath('//tr[@class="dmain_right_tab_list"][1]/td[7]/text()')
danwei = selector.xpath('//tr[@class="dmain_right_tab_list"][1]/td[10]/text()')
area = selector.xpath('//tr[@class="dmain_right_tab_list"][1]/td[11]/text()')

table.append({'date':date[0],'name':name[0],'num':num[0],'price':price[0],'danwei':danwei[0],'area':area[0]})
print(table)