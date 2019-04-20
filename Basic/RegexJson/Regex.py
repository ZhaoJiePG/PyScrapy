# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

a = 'C|C++|Java|C#|Python|Javascript'

# 普通字符
# 返回正则匹配的列表 findall
r = re.findall('Python', a)
if len(r) != 0:
    print('字符串包含Python')
print(r)

a = 'C0C++7Java8C#9Python6Javascript'

# 元字符
# 概括字符集
# 正则匹配数字
print(re.findall('\d', a))
print(re.findall('[0-9]+', a))
# 匹配非数字
print(re.findall('[^0-9]', a))
# 匹配所有单词字符
print(re.findall('\w', a))
# 匹配所有非单词字符
print(re.findall('\W', a))
# 匹配所有非空白字符
print(re.findall('\s', a))
# 匹配所有空白字符
print(re.findall('\S', a))
# 正则匹配非数字
print(re.findall('\D', a))
print(re.findall('[a-z,A-Z]', a))

s = 'abc,acc,adc,aec,afc,ahc'
# 匹配字符c或者a或者f [中间表示或的关系]
print(re.findall('a[cdf]c', s))
print(re.findall('a[c-f]c', s))
# 匹配取反 [^取反]
print(re.findall('a[^cfd]c', s))

# 匹配数量,贪婪
a = 'python123 java456 php777'
print(re.findall('[a-z]{3}', a))
print(re.findall('[a-z]{3,6}', a))

# 非贪婪
print(re.findall('[a-z]{3,6}?', a))

'''
数量词：
* 匹配0次或者无限次
+ 匹配1次或者无限次
? 匹配0次或者一次
'''
a = 'python0python1pythonn2'
print(re.findall('python*', a))
print(re.findall('python+', a))
print(re.findall('python?', a))
# 非贪婪
print(re.findall('python{1,2}?', a))

# 边界匹配
qq = '1000000001'
# 4-8
print(re.findall('^\d{4,8}$', qq))
print(re.findall('^000', qq))
print(re.findall('0001$', qq))

# 组
a = 'PythonPythonPythonPythonPythonPythonJS'
print(re.findall('(Python){3}(JS)', a))

'''
模式 ：
I 忽略大小写
S 支持对点号的支持
. 匹配除\n符外的其他字符

'''
la = 'PythonC#\nJava'
print(re.findall('c#', la, re.I))
print(re.findall('c#.{1}', la, re.I | re.S))
