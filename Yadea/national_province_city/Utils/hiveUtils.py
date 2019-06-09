# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyhive import presto
host='10.149.1.210'
port='8080'
cursor = presto.connect('10.149.1.210').cursor( port=port)
cursor.execute('SELECT * FROM test.test LIMIT 10')
print(cursor.fetchone())
print(cursor.fetchall())