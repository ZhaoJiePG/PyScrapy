# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# List 列表
print(type([1, 2, 3, 4]))
print(type(["world", 'hello', 3, 4, True, False]))
print(type([[1, 2], [3, 4], [True, False]]))

list = ["星月打击", "苍白之瀑", "月之降临", "月神冲刺"]
# 得到字符串
print(list[0])
# 得到列表
print(list[0:2])
print(list[1:3])
print(list[:-3])

# 追加列表的值
print(list + ["1", "2"])
print(list * 2)

# 更改列表的值
