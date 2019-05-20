# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import redis

# 1.连接数据库 key - value
client = redis.StrictRedis(host='127.0.0.1',port=6379)

# 2.设置key
key = 'pyone'

# 3.string增加
result = client.set(key,"1")

# 4.string删除
result = client.delete()

# 5.修改
result = client.set(key,"2")

# 6.查询
result = client.get(key)
