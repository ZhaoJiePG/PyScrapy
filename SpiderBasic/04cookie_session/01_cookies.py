# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request

# 1.数据url
url = 'https://mail.qq.com/cgi-bin/frame_html?sid=LiblK-GYO40zaC5y&r=7fea288cf954ad2151192eaf0a343903'
# 2.添加请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

# 3.构建请求对象
request = urllib.request.Request(url,headers=headers)

# 4.发送请求对象
response = urllib.request.urlopen(request)

# 5.读取数据
data = response.read()
print(type(data))

# 保存到文件中 验证数据
with open('01cook.html', 'wb') as f:
    f.write(data)

