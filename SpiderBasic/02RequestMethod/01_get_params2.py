# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import string


def get_params():
    url = "http://www.baidu.com/s?wd="

    params = {
        "wd": "中文",
        "key": "zhao",
        "value": "jie"
    }

    # 转译字典为字符串
    str_urls = urllib.parse.urlencode(params)
    print(str_urls)
    final_result = url + str_urls
    print(final_result)

    # 转译url为ascll码
    end_url = urllib.parse.quote(final_result, safe=string.printable)
    print(end_url)

    response = urllib.request.urlopen(end_url)
    data = response.read().decode("utf-8")
    print(data)


get_params()