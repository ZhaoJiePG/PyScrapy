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

cookies = session.cookies

# 二次请求的网址
url='http://www.chinaccm.cn/PriceData/PriceData.aspx?Type=DATA_NATIONALPRICE%2c%E5%9B%BD%E5%86%85%E4%BB%B7%E6%A0%BC&Cata=1&scode=3401&limit=Grade%2cM250E%3b&dshow=SuppName%2cGrade%2cDate%2cPrice'


# session接受调用cookie
response = requests.get(url=url, headers=headers,cookies=cookies)
context = response.text

# 解析
table = []
# 解析
selector = etree.HTML(context)
date = selector.xpath('//tr[@class="dmain_right_tab_list"][1]/td[3]/text()')
name = selector.xpath('//tr[@class="dmain_right_tab_list"][1]/td[1]/text()')
num = selector.xpath('//tr[@class="dmain_right_tab_list"][1]/td[2]/text()')
res_name = str(name[0]) + '(' + str(num[0]) + ')'
price = selector.xpath('//tr[@class="dmain_right_tab_list"][1]/td[4]/text()')
table.append({'name': res_name, 'date': date[0], 'price': price[0]})



print(table)