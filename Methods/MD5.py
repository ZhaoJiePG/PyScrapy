# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import hashlib

md = hashlib.md5()  # 构造一个md5
md.update('date=1559175611000,1559176211000&ourSecretKey=outyadeaapi'.encode())
print(md.hexdigest())  # 加密后的字符串

# 加密库
#   撞库
# 加盐
def md5_passwd(str, salt='123456'):
    # satl是盐值，默认是123456
    str = str + salt
    import hashlib
    md = hashlib.md5()  # 构造一个md5对象
    md.update(str.encode())
    res = md.hexdigest()
    return res

    # s='jmy123'
    # new_s='jmy123问'.encode() #字符串变成byetes类型
    # print('encode....',new_s)
    # print('decode',new_s.decode()) #

