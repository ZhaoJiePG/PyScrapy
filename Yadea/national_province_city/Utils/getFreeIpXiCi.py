# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import re

import pymysql
import requests
from lxml import etree

from Yadea.national_province_city.Utils.getRandomUserAgent import getRandomUserAgent

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='spider', charset='utf8')
cursor = conn.cursor()


# cursor.execute(
#     "delete from ip_proxy"
# )
# conn.commit()

# 随机请求头
headers = getRandomUserAgent()


# 保存高匿代理ip
def save_high_ni_ips():
    for i in range(1, 2):
        url = 'http://www.xicidaili.com/wt/{0}'.format(i)
        proxy = {'http': 'http://115.159.31.195:8080'}
        response = requests.get(url=url, headers=headers,proxies=proxy)
        data = response.content.decode("UTF-8")

        selector = etree.HTML(data)
        # 通用xpath地址
        tables = selector.xpath('//table[@id="ip_list"]//tr')

        # 保存高匿ip地址
        ip_high_ni = []

        # 循环爬取table标签下的tr,从第二个开始
        for cols in tables[1:]:
            ip = cols.xpath('./td[2]/text()')
            port = cols.xpath('./td[3]/text()')
            ni_type = cols.xpath('./td[5]/text()')
            alive_time = cols.xpath('./td[9]/text()')

            if ni_type == ['高匿'] and re.findall('分钟', str(alive_time)):
                ip_high_ni.append((ip, port, ni_type, alive_time))
                # print('高匿代理ip')
            else:
                # print('透明ip')
                continue

        for ip_info in ip_high_ni:
            # 提交数据库，保存高匿ip
            cursor.execute(
                "INSERT into ip_proxy(ip,port,alive_time) VALUES('{0}','{1}','{2}')".format(str(ip_info[0])[2:-2],
                                                                                            str(ip_info[1])[2:-2],
                                                                                            str(ip_info[3])[2:-2])
            )
            conn.commit()
            print(ip_high_ni)

save_high_ni_ips()

# 获取动态ip实列
class getHighniIP(object):
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
            return str(res_ip)
        else:
            return self.get_random_ip

try:
    a = getHighniIP().get_random_ip()
    print(a)
except:
    # 关闭数据库连接
    conn.close()

