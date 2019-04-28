# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

# https是带有第三方CA证书的
# 解决方案：告诉web忽略证书 访问
url = 'https://www.12306.cn/mormhweb'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

response = requests.get(url=url,headers=headers,verify=False)
data = response.content.decode("utf-8")

print(data)