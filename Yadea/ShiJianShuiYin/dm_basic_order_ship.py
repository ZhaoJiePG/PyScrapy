# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
时间水印操作mysql:
1.hive里原表old和new分区更新
2.更新mysql里的old，new表
3.从old表更新展现表，new-old更新diff表
4.展现表+diff 更新展现表
'''
import datetime
from time import sleep
import pymysql

# 基本参数
etl_time = 600
sleep_time = 10
# 当前时间
now_time = datetime.datetime.now()
print('开始时间:'+ str(now_time))

add_hour = datetime.datetime.now()+datetime.timedelta(hours=((9+(30/60))/60))
print('结束时间'+ str(add_hour))


# 获取连接
def getcoon():
    config = dict(host='10.149.1.154', user='root', password='root',
                  cursorclass=pymysql.cursors.DictCursor)

    # 建立连接
    conn = pymysql.Connect(**config)

    # 自动确认commit True
    conn.autocommit(1)

    return conn


# 查询
def query(sql, conn):
    # 设置光标
    cursor = conn.cursor()

    # 选择连接database
    conn.select_db('timewatermark')
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close()
    return data


# 关闭连接
def closecoon(conn):
    conn.close()


if __name__ == '__main__':
    conn = getcoon()

    # 更新前端表
    while (add_hour-datetime.datetime.now()).seconds <600:
        print((add_hour-datetime.datetime.now()).seconds)
        print(datetime.datetime.now())
        update_sql = '''
                     update
            timewatermark.dm_basic_order_ship as a
        inner join(
            SELECT
                a.num,
                a.name,
                (a.lingshou+b.lingshou) as lingshou,
                (a.lingshou_year+b.lingshou_year) as lingshou_year,
                (a.dingdan+b.dingdan) as dingdan,
                (a.fahuo+b.fahuo) as fahuo,
                (a.fahuo_year+b.fahuo_year) as fahuo_year,
                (a.ruku+b.ruku) as ruku,
                (a.m_paichan+b.m_paichan) as m_paichan,
                (a.d_paichan+b.d_paichan) as d_paichan,
                (a.kucun+b.kucun) as kucun,
                (a.in_kucun+b.in_kucun) as in_kucun,
                (a.out_kucun+b.out_kucun) as out_kucun,
                now() as etl_date,
                a.type_id
            from
                timewatermark.dm_basic_order_ship as a
            left JOIN timewatermark.dm_basic_order_ship_diff as b on
                a.name = b.name) c on
            a.name = c.name set
            a.lingshou = c.lingshou,
            a.lingshou_year = c.lingshou_year,
            a.dingdan = c.dingdan,
            a.fahuo = c.fahuo,
            a.fahuo_year = c.fahuo_year,
            a.ruku = c.ruku,
            a.m_paichan = c.m_paichan,
            a.d_paichan = c.d_paichan,
            a.kucun = c.kucun,
            a.in_kucun = c.in_kucun,
            a.out_kucun = c.out_kucun,
            a.etl_date = c.etl_date;
            '''
        print('修改成功')
        # 执行修改
        query(update_sql,conn)
        # 休眠2s
        sleep(sleep_time)
    else:
        print("结束。。。")
    print(datetime.datetime.now())

    # 关闭连接
    closecoon(conn)
