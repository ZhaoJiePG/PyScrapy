# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re

from lxml import etree

import requests

url = 'https://www.lagou.com/zhaopin/Java/'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'cookie':'JSESSIONID=ABAAABAAAGFABEF69873519ABB60A92592B17F815B314F5; user_trace_token=20190530144402-8a2c5672-fc05-4750-bcb0-bef971f0003e; _ga=GA1.2.766086889.1559198643; _gid=GA1.2.1822315135.1559198643; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1559198644; LGUID=20190530144402-4ff44da1-82a6-11e9-a17e-5254005c3644; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; index_location_city=%E4%B8%8A%E6%B5%B7; LGSID=20190530154804-41805b49-82af-11e9-a846-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F; TG-TRACK-CODE=index_user; _gat=1; LG_LOGIN_USER_ID=99d622f4ca6e041ae7d1bcd0e789d43065493116fea5e39078a4f1434c58f0f4; _putrc=4E631D5E20439847123F89F2B170EADC; login=true; unick=%E6%9D%8E%E4%BD%B3%E5%9D%A4; gate_login_token=a00c488295d51842f95c20e464bd2a2a169c933c3e733130b352e9fa0a634f38; X_HTTP_TOKEN=9a20e5e30f512c7f20230295511d2889aed8cf9afd; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1559203203; LGRID=20190530160002-edc7fca4-82b0-11e9-a846-525400f775ce; SEARCH_ID=fcc58e24cbbc418ca150409e9f42cb16'
}

response = requests.get(url,headers=headers)
content = response.text

selector = etree.HTML(content)

# joblist = selector.xpath('//ul[@class="item_con_list"]/li[1]//h3/text()')
joblist = selector.xpath('//ul[@class="item_con_list"]/li[1]//h3/text()')
print(joblist)

job = []
for i in range(1,2):
    jobname_path = './li[{0}]//h3/text()'.format(i)

    # jobname = joblist.xpath(jobname_path)
    print(jobname_path)

    # job.append(jobname)

# print(job)
    # print(len(jobname))
    # jobarea = i.xpath('//a[@class="position_link"]/span[@class="add"]/em/text()')
    # print(jobarea)
    # print(len(jobarea))
    # # publishtime = i.xpath('//span[@class="format-time"]/text()')
    # salary = i.xpath('//span[@class="money"]/text()')
    # print(salary)
    # print(len(salary))
    #
    # workexperience = i.xpath('//div[@class="li_b_l"]/text()')
    # res1 = [re.findall('([\u4e00-\u9fa5]+[0-9]-[0-9].*)',x) for x in workexperience]
    # res = []
    # for i in res1:
    #     # print(i)
    #     if i != []:
    #         print(i)
    #         res.append(res)
    # print(res)
    # print(len(res))