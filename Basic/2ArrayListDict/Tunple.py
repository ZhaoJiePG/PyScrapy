# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 元祖
tunple = (1, 2, 3, 4, 5)
print(type(tunple))

print(tunple * 3)
print(tunple[1:3])
print(tunple + ("q", "abc"))

# 是否存在
print(3 in tunple)
print(3 not in tunple)
print(10 in tunple)

# 长度
print(len(tunple))

# 最大值
print(max(tunple),min(tunple))

# ascll码
print(max("helloworld"))
print(ord("w"),ord(" "))