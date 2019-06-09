# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from lxml import etree

import requests
import re

# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'cookie':'SMM_device_id=a1a205c2-2b73-539b-a6b7-3f001bfd540b; _ga=GA1.2.1753996494.1559692706; _gid=GA1.2.1153050512.1559692706; SMM_session_id=11167d04-6d51-526c-88a6-52d6fc49ee8e; SMM_session_start_timestamp=1559779558317; Hm_lvt_9734b08ecbd8cf54011e088b00686939=1559692696,1559698828,1559698961,1559779558; Hm_lvt_50b0b45724f4f39e2a94cb8af0e9b547=1559692706,1559779558; Hm_lpvt_50b0b45724f4f39e2a94cb8af0e9b547=1559779558; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lpvt_9734b08ecbd8cf54011e088b00686939=1559779578; SMM_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjZWxscGhvbmUiOiIxMzYxNjY4MzM1MCIsImNvbXBhbnlfaWQiOjAsImNvbXBhbnlfc3RhdHVzIjowLCJjcmVhdGVfYXQiOjE1NTk3Nzk3MjUsImVtYWlsIjoia2FpamlhbmcudGFvQGNoaW5heGluemhpLmNvbSIsImVuX2VuZF90aW1lIjowLCJlbl9yZWdpc3Rlcl9zdGVwIjoxLCJlbl9yZWdpc3Rlcl90aW1lIjowLCJlbl9zdGFydF90aW1lIjowLCJlbl91c2VyX3R5cGUiOjAsImVuZF90aW1lIjoxNTgyNzMyNzk5LCJpc19tYWlsIjowLCJpc19waG9uZSI6MSwibGFuZ3VhZ2UiOiJjbiIsImx5X2VuZF90aW1lIjowLCJseV9zdGFydF90aW1lIjowLCJseV91c2VyX3R5cGUiOjAsInJlZ2lzdGVyX3RpbWUiOjEzNjIwMTk1NjIsInN0YXJ0X3RpbWUiOjE1MTk1NzQ0MDAsInVzZXJfaWQiOjQxMTU5NywidXNlcl9uYW1lIjoieGluemhpZGlhbmppMDIiLCJ1c2VyX3R5cGUiOjIsInp4X2VuZF90aW1lIjowLCJ6eF9zdGFydF90aW1lIjowLCJ6eF91c2VyX3R5cGUiOjB9.VQd_gll5uCpMkabd5_3n308KqEwdKVuuQdoSRZe42Dg'
}
#
# # session模拟用户登陆=cookiejar
# session = requests.session()
#
# # 模拟的登陆页面
# post_url = "https://user.smm.cn/login"
#
# # post请求保存的账号密码
# post_data = {"user_name": "xinzhidianji02", "password": "123456"}
#
# # 模拟登陆
# responsee = session.post(url=post_url, data=post_data, headers=headers)
# # print(responsee.content.decode())

# 二次请求的网址
url = 'https://hq.smm.cn/tong/category/201102250376'

# session接受调用cookie
response = requests.get(url=url, headers=headers)
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
