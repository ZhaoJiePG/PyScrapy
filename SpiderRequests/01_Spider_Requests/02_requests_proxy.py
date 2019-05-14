# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

url = 'http://www.baidu.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
free_proxy={
    'http':'116.209.55.195:9999'
}

response = requests.get(url=url,headers=headers,proxies = free_proxy)
print(response.status_code)