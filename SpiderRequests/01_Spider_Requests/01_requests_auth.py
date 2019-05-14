# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

url = ''
# 发送post请求
data = {

}
response = requests.post(url=url,data=data)

# 内网 认证
auth = {"",""}
reponse = requests.get(url=url,auth=auth)