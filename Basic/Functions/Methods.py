# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
from functools import reduce
# map
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6, 7]

def square(x):
    return x * x

for x in list_x:
    square(x)

r = map(square,list_x)
print(type(r))
print(list(r))

# 改写lambda
r = map(lambda x : x*x,list_x)
print(list(r))

# 多参数,长度取决于参数较小的
r = map(lambda x ,y : x*x + y,list_x,list_y)
print(list(r))

# reduce:累加聚合
r = reduce(lambda x,y:x+y,list_x,2)
print(r)

# filter
r = filter(lambda x : True if x > 3 else False,list_x)
print(list(r))
list_u = ['a','B','c','D']
r = filter(lambda x : len(re.findall('\d',x))>0 ,list_u)
print(r)