# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import pandas as pd
import pymysql
from lxml import etree
import requests

# 获取csv网址
def getUrlList(csv_path, url_name):
    # 读取csv文件
    csv_file = open(csv_path, 'rb').read().decode('utf-8')
    # 保存地区和url
    url_list = []
    for x in csv_file.split('\r\n'):
        url_info = x.split(',')
        # 判断需要的网址
        if url_info[1] == url_name:
            url_list.append({url_info[1]: [url_info[0], url_info[2]]})

    return url_list

# 解析中国商务网
def praseChinaBusiness(url_list):
    # 定义请求头
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'cookie': "CompNew=32557%40DATA_NATIONALPRICE%40Date%2cSuppName%2cSpec%2cSpecModelName%2cGrade%2cPrice%2cPriceXXChange%2cBottomPrice%2cHighPrice%2cAvgPrice%2cAvgPriceXXChange%2cProvinceName%2cPriceTell%2cPriceUnit%2cMarketName%2cAreaName%2cCityName%2cPortName%2cLocalityName%2cContract%2cPlaceOfDelivery%2cMarks%2cMainPrice|铝合金|CarID_32557&&&; UserCount=50F+zk6pYMYaLB9DEbsmQVXIH7avJgZdFCNIlVNWP2mRuhYcc9jRJu8VOgNG54oSUkPk6IFXC90fKrXa/Ytnw0U67INIqgVL; Hm_lvt_8c905ec8d12584debce091e1b8c39fc3=1559366230,1559446331,1559693340; ASP.NET_SessionId=hgicziuefdbqo1el1cydwxeb; Hm_lvt_55f4388cb1206cf827c03a4f9ff5cbd0=1559693277,1559706263,1559780001,1560042660; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; CustInfo=50F+zk6pYMasBvSZvR0fHxL74yYnRHxzr0CM6qmxg1ehqKBuSVAiwCzKN7yZQ9Os1NFsz53hUkpVpnGa52DuRNzy3bWItuQphpxFIH1wLShgQ3uQCJzosWNx+cyE2lmyLfjpG+r5bptQ7jyyo1+dYGfluIn7vnEceNCaiS/3q0w=; Hm_lpvt_55f4388cb1206cf827c03a4f9ff5cbd0=1560047871"
    }
    url = url_list['中华商务网'][1]
    print(url)

    # session接受调用cookie
    response = requests.get(url=url, headers=headers)
    context = response.text

    # with open('login.txt','r') as f:
    #     f.write(context)

    # 解析
    selector = etree.HTML(context)

    date = selector.xpath('//tr[@class="dmain_right_tab_list"][2]/td[2]/text()')
    print(date)

# 解析上海有色网
def praseShangHaiYouSe(url_list):
    # 保存表数据
    table = []

    # 定义请求头
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'cookie': 'SMM_device_id=a1a205c2-2b73-539b-a6b7-3f001bfd540b; _ga=GA1.2.1753996494.1559692706; _gid=GA1.2.1153050512.1559692706; SMM_session_id=11167d04-6d51-526c-88a6-52d6fc49ee8e; SMM_session_start_timestamp=1559779558317; Hm_lvt_9734b08ecbd8cf54011e088b00686939=1559692696,1559698828,1559698961,1559779558; Hm_lvt_50b0b45724f4f39e2a94cb8af0e9b547=1559692706,1559779558; Hm_lpvt_50b0b45724f4f39e2a94cb8af0e9b547=1559779558; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lpvt_9734b08ecbd8cf54011e088b00686939=1559779578; SMM_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjZWxscGhvbmUiOiIxMzYxNjY4MzM1MCIsImNvbXBhbnlfaWQiOjAsImNvbXBhbnlfc3RhdHVzIjowLCJjcmVhdGVfYXQiOjE1NTk3Nzk3MjUsImVtYWlsIjoia2FpamlhbmcudGFvQGNoaW5heGluemhpLmNvbSIsImVuX2VuZF90aW1lIjowLCJlbl9yZWdpc3Rlcl9zdGVwIjoxLCJlbl9yZWdpc3Rlcl90aW1lIjowLCJlbl9zdGFydF90aW1lIjowLCJlbl91c2VyX3R5cGUiOjAsImVuZF90aW1lIjoxNTgyNzMyNzk5LCJpc19tYWlsIjowLCJpc19waG9uZSI6MSwibGFuZ3VhZ2UiOiJjbiIsImx5X2VuZF90aW1lIjowLCJseV9zdGFydF90aW1lIjowLCJseV91c2VyX3R5cGUiOjAsInJlZ2lzdGVyX3RpbWUiOjEzNjIwMTk1NjIsInN0YXJ0X3RpbWUiOjE1MTk1NzQ0MDAsInVzZXJfaWQiOjQxMTU5NywidXNlcl9uYW1lIjoieGluemhpZGlhbmppMDIiLCJ1c2VyX3R5cGUiOjIsInp4X2VuZF90aW1lIjowLCJ6eF9zdGFydF90aW1lIjowLCJ6eF91c2VyX3R5cGUiOjB9.VQd_gll5uCpMkabd5_3n308KqEwdKVuuQdoSRZe42Dg'
    }

    for i in range(0, len(url_list)):
        # 请求的网址
        url = url_list[i]['上海有色网'][1]

        # session接受调用cookie
        response = requests.get(url=url, headers=headers)
        context = response.text

        # 解析
        selector = etree.HTML(context)
        name = selector.xpath('//h3[@class="chart-data-left-pdt"]/text()')
        date = selector.xpath('//ul[@class="history-t-body"]/li[1]/div[1]/text()')
        price = selector.xpath('//ul[@class="history-t-body"]/li[1]/div[3]/text()')

        # 保存数据
        table.append({'name': name[0], 'area': str(url_list[i]['上海有色网'][0]), 'date': date[0], 'price': price[0]})

    return table

# 保存csv格式
def saveAsCsv(data, name):
    df = pd.DataFrame(data)
    df.to_csv('./data/{0}.csv'.format(name), sep=',', header=True, index=False, encoding='utf-8')
    print("保存成功")

# 保存数据到mysql
def saveToMysql(data):
    config = dict(host='10.149.1.154', user='root', password='root',
                  cursorclass=pymysql.cursors.DictCursor)
    # 建立连接
    conn = pymysql.Connect(**config)
    print(conn)
    # 自动确认commit True
    conn.autocommit(1)
    # 设置光标
    cursor = conn.cursor()

    def make_table_sql(df):
        columns = df.columns.tolist()
        types = df.ftypes
        # 添加id 制动递增主键模式
        make_table = []
        for item in columns:
            if 'int' in types[item]:
                char = item + ' BIGINT'
            elif 'float' in types[item]:
                char = item + ' FLOAT'
            elif 'object' in types[item]:
                char = item + ' VARCHAR(255)'
            elif 'datetime' in types[item]:
                char = item + ' DATETIME'
            make_table.append(char)
        return ','.join(make_table)


    def csv2mysql(db_name, table_name, df):
        # 创建database
        cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(db_name))
        # 选择连接database
        conn.select_db(db_name)
        # 创建table
        cursor.execute('DROP TABLE IF EXISTS {}'.format(table_name))
        cursor.execute('CREATE TABLE {}({})'.format(table_name,make_table_sql(df)))
        # 提取数据转list 这里有与pandas时间模式无法写入因此换成str 此时mysql上格式已经设置完成
        # df['日期'] = df['日期'].astype('str')
        values = df.values.tolist()
        # 根据columns个数
        s = ','.join(['%s' for _ in range(len(df.columns))])
        # executemany批量操作 插入数据 批量操作比逐个操作速度快很多
        cursor.executemany('INSERT INTO {} VALUES ({})'.format(table_name,s), values)

    csv2mysql('test','RawPrice',data)
    conn.close()

if __name__ == '__main__':
    chinaBusinessUrl = getUrlList('./Data/RawUrl.csv', '中华商务网')[1]
    # 获取上海有色网url
    shangHaiYouSeUrl = getUrlList('./Data/RawUrl.csv', '上海有色网')
    # 获取上海有色网数据
    shangHaiYouSeData = praseShangHaiYouSe(shangHaiYouSeUrl)
    # 保存csv数据
    saveAsCsv(shangHaiYouSeData,'上海有色网')
    data1 = pd.read_csv('./Data/上海有色网.csv')
    data2 = pd.read_csv('./Data/中华商务网.csv')
    # 取数据交集
    data = pd.merge(data1,data2,how='outer')
    print(data)
    # 保存mysql
    saveToMysql(data)


    # praseChinaBusiness(url_list)
