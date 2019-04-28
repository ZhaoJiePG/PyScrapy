# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
直接获取 个人中心的页面
手动粘贴 复制 PC 抓包的cookie
放在 request对象的请求头里面
'''
import urllib.request

# 1.数据url
url = 'https://www.yaozh.com/member/'
# 2.添加请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Cookie':'acw_tc=707c9f9815559826879482128e0233e365fd1f84bb6b13c7385503c352ff0a; PHPSESSID=f9aud0uq3bhevgo7mcpmogri43; _ga=GA1.2.1988384091.1555983167; _gid=GA1.2.1382764641.1555983167; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1555983302; yaozh_logintime=1555983310; yaozh_user=735753%09aliexjj; yaozh_userId=735753; db_w_auth=662042%09aliexjj; UtzD_f52b_saltkey=RVPUuCUa; UtzD_f52b_lastvisit=1555979711; UtzD_f52b_lastact=1555983311%09uc.php%09; UtzD_f52b_auth=7897fktceB3XXI05Gy8NKmn%2BkmBk%2FECLSsHi7iMh0LmPRioTvH1HT7bb9wCzA77stgKsvILImASQpRl%2FJ9AwZ53dlWs; yaozh_uidhas=1; yaozh_mylogin=1555983324; acw_tc=707c9f9815559826879482128e0233e365fd1f84bb6b13c7385503c352ff0a; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1555983168%2C1555983259%2C1555983302'
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

