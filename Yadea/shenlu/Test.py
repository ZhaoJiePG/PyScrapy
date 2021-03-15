# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests

url = 'https://yadea.udesk.cn/open_api_v1/log_in'
# h = {'Content-type':'application/json'}
d = {'email': 'zhijin_d@yadea.com.cn', 'password': 'zy123456'}
r = requests.post(url, data=d).headers

print(r)
