# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
import requests

url = 'http://news.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
res = requests.get(url=url,headers=headers)
data = res.content.decode("utf-8")

# 正则解析数据
# 解析每个新闻的title,url
# <a href="http://politics.people.com.cn/GB/8198/426296/index.html" target="_blank" mon="r=1">壮丽70年</a>
parttern = re.compile('(<a href="(.*?)" target="_blank" mon="(.*?)">(.*?)</a>)',re.S)
result = parttern.findall(data)

# parttern = re.compile('<a href="(.*?)" title="(.*?)"')
# result = parttern.findall(str(result))
# print(result)
# res_dict = {list[0]:list[1] for list in result}

print(result)


# with open('news.html','w',encoding="utf-8")as f:
#     f.write(result)