# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 函数
print()

# 保留小数
a = 1.123
print(round(a, 2))


# 自定义函数
def sum(a, b):
    res = a + b
    return res


print(sum(1, 2))

# 设置递归的最大格式
import sys

sys.setrecursionlimit(1000000)


# 返回多个值
def damage(skill1, skill2):
    return skill1 * 2, skill2 * 3


res = damage(100, 200)
print(res)
print(type(res))

# 序列解包
s1, s2 = damage(1, 2)
print(s1, s2)

a, b, c = 1, 2, 3
d = a, b, c
print(d)

# 链式赋值
a = b = c = 1

'''
参数：
1.必须参数
2.关键词参数
'''
print(sum(a=2, b=2))
