# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
它从任何暴露数组接口的对象，或从返回数组的任何方法创建一个ndarray。
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
上面的构造器接受以下参数：
object 任何暴露数组接口方法的对象都会返回一个数组或任何(嵌套)序列。
dtype 数组的所需数据类型，可选。
copy 可选，默认为true，对象是否被复制。
order C(按行)、F(按列)或A(任意，默认)。
subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
ndimin 指定返回数组的最小维数。
'''

import numpy as np

a = np.array([1, 2, 3])
print(a)

# 二维数据
b = np.array([[1, 2], [3, 4]])
print(b)

# 最小维度
c = np.array([1, 2, 3, 4, 5], ndmin=1)
print(c)

# dtype参数,是否显示复数
d = np.array([1, 2, 3], dtype=complex)
print(d)
