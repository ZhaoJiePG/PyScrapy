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
post_url = "https://user.smm.cn/login"

# post请求保存的账号密码
post_data = {"session_id": "aa02a61b-60a3-5ade-8596-6bd420ad4e03"
    ,"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjZWxscGhvbmUiOiIxMzYxNjY4MzM1MCIsImNvbXBhbnlfaWQiOjAsImNvbXBhbnlfc3RhdHVzIjowLCJjcmVhdGVfYXQiOjE1NjA5NTA5OTEsImVtYWlsIjoia2FpamlhbmcudGFvQGNoaW5heGluemhpLmNvbSIsImVuX2VuZF90aW1lIjowLCJlbl9yZWdpc3Rlcl9zdGVwIjoxLCJlbl9yZWdpc3Rlcl90aW1lIjowLCJlbl9zdGFydF90aW1lIjowLCJlbl91c2VyX3R5cGUiOjAsImVuZF90aW1lIjoxNTgyNzMyNzk5LCJpc19tYWlsIjowLCJpc19waG9uZSI6MSwibGFuZ3VhZ2UiOiJjbiIsImx5X2VuZF90aW1lIjowLCJseV9zdGFydF90aW1lIjowLCJseV91c2VyX3R5cGUiOjAsInJlZ2lzdGVyX3RpbWUiOjEzNjIwMTk1NjIsInN0YXJ0X3RpbWUiOjE1MTk1NzQ0MDAsInVzZXJfaWQiOjQxMTU5NywidXNlcl9uYW1lIjoieGluemhpZGlhbmppMDIiLCJ1c2VyX3R5cGUiOjIsInp4X2VuZF90aW1lIjowLCJ6eF9zdGFydF90aW1lIjowLCJ6eF91c2VyX3R5cGUiOjB9.FGc2DdHcUpw-0b9WTZo8MC5oGRW6I38cMElmBtL_DEc"}

# 模拟登陆
responsee = session.post(url=post_url, data=post_data, headers=headers)
# print(responsee.content.decode())

cookies = session.cookies

# 二次请求的网址
url = 'https://hq.smm.cn/tong/category/201102250376'

# session接受调用cookie
response = requests.get(url=url, headers=headers,cookies=cookies)
context = response.text

# 解析
selector = etree.HTML(context)
table = []

date = selector.xpath('//ul[@class="history-t-body"]/li[1]/div[1]/text()')
range = selector.xpath('//ul[@class="history-t-body"]/li[1]/div[2]/text()')
price = selector.xpath('//ul[@class="history-t-body"]/li[1]/div[3]/text()')
up = selector.xpath('//ul[@class="history-t-body"]/li[1]/div[4]/text()')

table.append({'date':date[0],'range':range[0],'price':price[0],'up':up[0]})

print(table)
