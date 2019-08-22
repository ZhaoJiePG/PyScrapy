# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyhive import hive

conn = hive.Connection(host='10.149.1.202', port=10000, username='root', database='dm')
cursor = conn.cursor()

cursor.execute('show tables')
for cur in cursor:
    print(cur)

import sasl
# 下面是官网代码：
# from pyhive import presto  # or import hive
# cursor = presto.connect('localhost').cursor()
# cursor.execute('SELECT * FROM my_awesome_data LIMIT 10')
# print(cursor.fetchone())

