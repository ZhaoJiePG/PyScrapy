# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import re

import pymysql
import requests
from lxml import etree

from Yadea.national_province_city.Utils.getRandomUserAgent import getRandomUserAgent

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='spider')
cursor = conn.cursor()


# cursor.execute(
#     "delete from ip_proxy"
# )
# conn.commit()

# 随机请求头
headers = getRandomUserAgent()


# 保存高匿代理ip
def save_high_ni_ips():
    # 存储ip的集合
    ip_list=[]

    for i in range(1, 10):
        url = 'http://ip.zdaye.com/dayProxy/2019/5/{0}.html'.format(i)
        proxy = {'http': 'http://36.7.89.233:8060'}
        response = requests.get(url=url, headers=headers,proxies=proxy)
        data = response.content.decode("UTF-8")
        selector = etree.HTML(data)

        #爬取ip的标签
        for i in range(2,15):
            # 获取xpath地址
            xpath= '//div[@class="threadblock_list"]/div[@class="thread_item"][{0}]//p/text()'.format(i)
            xpath_path = selector.xpath(xpath)
            res = re.findall('([1-9][1-9]+.[0-9]+.[0-9]+.[0-9]+:[0-9]+)',str(xpath_path))

            #判断是否爬取到数据
            if(len(res) != 0):
                for j in range(0,len(res)):
                    ip_list.append(res[j])

    # 保存到数据库
    for ip_info in ip_list:
        # 提交数据库，保存高匿ip
        cursor.execute(
            "INSERT into ip_proxy(ip) VALUES('{0}')".format(ip_info)
        )
        conn.commit()

# save_high_ni_ips()

# 获取动态ip实列
class get_IP(object):
    # 判断ip池数量


    # 判断ip是否有效
    def ip_is_valid(self, ip):
        try:
            proxy = {'http': ip}
            print(proxy)
            url = 'http://ip.chinaz.com/'
            response = requests.get(url=url, headers=headers,proxies=proxy,timeout=5)
            status_code = response.status_code
            print(status_code)

            #判断是否正常返回
            if(200 <= status_code < 300):
                return True
            else:
                return False

        except:
            print('ip无效')
            self.delete_unvlid_ip(ip)
            return False

    # 删除无效ip
    def delete_unvlid_ip(self,ip):
            delete_sql = 'DELETE FROM ip_proxy WHERE ip="{0}"'.format(ip)
            cursor.execute(delete_sql)
            conn.commit()
            print('删除成功')
            return True

    # 获取随机ip
    @property
    def get_random_ip(self):
        random_ip = 'SELECT ip FROM ip_proxy ORDER BY RAND() LIMIT 1;'
        cursor.execute(random_ip)
        res_ip = cursor.fetchone()[0]

        #判断ip是否成功
        valid_ip = self.ip_is_valid(res_ip)
        if valid_ip:
            return res_ip
        else:
            return self.get_random_ip

# proxy = get_IP().get_random_ip
# print(proxy)
# print(type(proxy))