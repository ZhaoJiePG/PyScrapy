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

add_hour = datetime.datetime.now()+datetime.timedelta(hours=((0+(30/60))/60))
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
        timewatermark.dm_erp_overview as a
        inner join(
        SELECT
            a.m_day,
            a.m_month,
            a.m_year,
            (a.day_sale_sum + b.day_sale_sum) as day_sale_sum,
            (a.month_sale_sum + b.month_sale_sum) as month_sale_sum,
            (a.year_sale_sum + b.year_sale_sum) as year_sale_sum,
            (a.day_pick_sum + b.day_pick_sum) as day_pick_sum,
            (a.month_pick_sum + b.month_pick_sum) as month_pick_sum,
            (a.year_pick_sum + b.year_pick_sum) as year_pick_sum,
            (a.day_stock_in_sum + b.day_stock_in_sum) as day_stock_in_sum,
            (a.month_stock_in_sum + b.month_stock_in_sum) as month_stock_in_sum,
            (a.year_stock_in_sum + b.year_stock_in_sum) as year_stock_in_sum,
            (a.stock_num + b.stock_num) as stock_num,
            (a.fund_restream + b.fund_restream) as fund_restream,
            (a.credit + b.credit) as credit,
            (a.receivable + b.receivable) as receivable,
            (a.sale_user_num + b.sale_user_num) as sale_user_num,
            (a.repair_user_num + b.repair_user_num) as repair_user_num,
            NOW() as etl_date
        from
            timewatermark.dm_erp_overview as a
        left JOIN timewatermark.dm_erp_overview_diff as b on
            a.m_day = b.m_day) c on
        a.m_day = c.m_day set
        a.m_month = c.m_month,
        a.m_year = c.m_year,
        a.day_sale_sum = c.day_sale_sum,
        a.month_sale_sum = c.month_sale_sum,
        a.year_sale_sum = c.year_sale_sum,
        a.day_pick_sum = c.day_pick_sum,
        a.month_pick_sum = c.month_pick_sum,
        a.year_pick_sum = c.year_pick_sum,
        a.day_stock_in_sum = c.day_stock_in_sum,
        a.month_stock_in_sum = c.month_stock_in_sum,
        a.year_stock_in_sum = c.year_stock_in_sum,
        a.stock_num = c.stock_num,
        a.fund_restream = c.fund_restream,
        a.credit = c.credit,
        a.receivable = c.receivable,
        a.sale_user_num = c.sale_user_num,
        a.repair_user_num = c.repair_user_num,
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

