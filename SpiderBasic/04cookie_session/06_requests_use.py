# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
# pip install requests

class RequestSpider(object):
    def __init__(self):
        url = 'http://www.baidu.com'
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }
        self.response = requests.get(url,headers=headers)

    def run(self):
        data = self.response.content

        # 1.获取请求头
        request_headers = self.response.request.headers
        print(request_headers)

        # 2.获取响应头
        response_headers = self.response.headers
        print(response_headers)

        # 3.获取响应码
        code = self.response.status_code
        print(code)

        # 4.请求的cookie
        request_cookie = self.response.request._cookies
        print(request_cookie)

        # 5.响应的cookie
        response_cookie = self.response.cookies
        print(response_cookie)

RequestSpider().run()