# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 系统保留关键字
import keyword

print(keyword.kwlist)

# 变量赋值
a = {1, 2, 3}
print(type(a))

a = [1, 2, 3]
a.append(4)
print(type(a))
a[1] = 2

# 显示内存地址 id函数
print(id(a))
a = 'hello'

# 追加元素
a = a + 'python'
print(id(a))

# 多维
a = (1,2,3,[1,2,4])
print(a[3][2])

