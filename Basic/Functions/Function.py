# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 匿名函数
def add(x, y):
    return x + y


# lambda表达式
f = lambda x, y: x + y
print(f(1, 2))

# 三元表达式
a = 1
b = 3
r = a if a > b else b
print(r)

