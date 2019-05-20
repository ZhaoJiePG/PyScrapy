# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql

try:
# 1.连接 数据库
    conn = pymysql.Connect(
        host = 'localhost',
        port=3306,
        db='animal',
        user='root',
        passwd='mysql',
        charset='utf-8'
    )

    # 2.建表 插入数据cursor()
    cur = conn.cursor()

    # 增加一条数据 科目表--GO语言
    # insert_sub = 'insert into subjects values(0,"GO语言")'
    # result = cur.execute(insert_sub)

    # 修改



    # 提交事务
    conn.commit()

    # 关闭游标
    cur.close()

    # 关闭连接
    conn.close()

except Exception as e:
    print(e)