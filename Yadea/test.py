# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num

for n in foo(0):
    print(n)
