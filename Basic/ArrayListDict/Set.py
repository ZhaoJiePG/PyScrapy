# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 集合:无序，不重复
set = {1, 2, 3, 4, 5, 6, 6}
print(type(set))
print(set)

# 无下表索引
# print(set[0])

print(1 in set)
print(1 not in set)

# 增加删除
print(set - {1, 2, 3})

# 交集
print(set & {1, 2, 3})

# 并集
print(set | {1,2,7})

# 空集合 dict
print(type({}))
