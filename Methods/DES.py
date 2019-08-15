# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from pyDes import des, CBC, PAD_PKCS5
import binascii

# 秘钥
KEY='mHAxsLYz'
def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_descrypt(s):
    """
    DES 解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de


a = '100%u7C73'
a= a.replace('%','\\').encode('utf-8')
print(a)
print(type(a))

a = '100%u7C73'.replace('%','\\')
a = bytes.decode(a)
print(a.encode('utf-8'))


print(type(a))
# a = str(a,encoding='utf-8')
print(a)
print(type(a))


s = '100\u7c73'
s.encode('UTF-8')
# s = s.decode().encode('unicode_escape')
print(s)
print(type(s))
