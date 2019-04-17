# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
    模块说明
'''
# If Else控制
mode = True

if mode:
    print('go to left')
else:
    print('go to right')
print('end if')

a = 1
b = 2
c = 2
d = []
if d:
    print('dd')
else:
    print('cc')

# 控制台读入 input()
USER = 'zj'
PASSWORD = '123456'

if USER == input() and PASSWORD == input():
    print('right')
else:
    print('false')

# 保持语句完整性
if True:
    pass #空语句/占位符

# if嵌套
if True:
    if True:
        print()
    print()
else:
    print()


