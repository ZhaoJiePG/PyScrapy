# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import string

def get_method_params():
    url = "http://www.baidu.com/s?wd="

    # 拼接字符串(汉字)
    name = "美女"
    final_url = url + name
    print(final_url)

    #需要转译中文为ascll码，将包含汉字的网址进行转译
    encode_new_url = urllib.parse.quote(final_url,safe=string.printable)
    print(encode_new_url)

    #使用代码发送网络请求
    response = urllib.request.urlopen(encode_new_url)
    print(response)
    # deEncodeError: 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128)

    # 读取数据
    data = response.read().decode("utf-8")
    print(data)

    # 保存到本地
    with open("02-encode.html","w",encoding="utf-8")as f:
        f.write(data)
get_method_params()
