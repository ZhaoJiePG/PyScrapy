# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

print('hello world')
print("hello world")

# 使用转译\符号
print("let's go")
print('let\'s go')

print('hello world' * 5)
print("""
hello world hello world
""")

print("c:\\north\\nest")
# 不会转译特殊符号
print(r"c:\north\nest")

print("helloworld"[0])
print("helloworld"[2])
print("helloworld"[-1])
print("helloworld"[-2])

# 截取字符
print("helloworld"[0:5])
print("helloworld"[5:0])
print("helloworld"[5:-2])
print("helloworld"[5:])
print("helloworld"[5:2])
# 步长
print("helloworld"[0:-1])
print("helloworld"[0:-2])

# 截取最后
print("hello world python php ruby"[-4:])
print("hello world python php ruby"[12:][0:6])