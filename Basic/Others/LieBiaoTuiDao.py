# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 列表推倒式
a = [1, 2, 3, 4, 5, 6, 7]

b = [i ** 2 for i in a]
print(b)

b = map(lambda x: x * x, a)
print(list(b))

# 条件筛选
b = [i ** 2 for i in a if i > 2]
print(b)

# 字典推倒式
students = {
    'zj':18,
    'aa':19,
    'bb':20
}

b = (k for k,v in students.items())
print(set(b))
