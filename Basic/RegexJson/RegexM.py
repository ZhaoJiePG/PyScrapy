# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

# 替换方法
la = 'PythonC#JavaPHPC#C#'
print(re.sub('C#', 'Go', la))
# 替换所有的
print(re.sub('C#', 'Go', la, 0))
# 只替换第一个
print(re.sub('C#', 'Go', la, 1))

l = la.replace('C#', 'Go')
print(l)


# sub替换函数
def convert(value):
    matched = value.group()
    return matched + '!!'


print(re.sub('C#', convert, la))

s = 'A8C3721D86'


def convertt(value):
    matchd = value.group()
    if int(matchd) >= 6:
        return '9'
    else:
        return '0'


print(re.sub('\d', convertt, s))

# match和search函数:都是只匹配一次

# match从字符串首字母开始匹配
print(re.match('\d', s))
# search搜索全局字符串，找到第一个返回
print(re.search('\d', s).group())
print(re.search('\d', s).span())

s = 'lif is short,i use python,i love python'
r = re.search('life(.*)python(.*)python', s)
print(r.group(0))
