# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 定义时复杂，调用时简洁
import time

# 装饰器
def decorator(func):
    # 封装
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)
    return wrapper

# 语法塘
@decorator
def f1():
    print("This is a function1")

@decorator
def f2(func_name1,func_name2,**name):
    print("This is a function2"+func_name1+func_name2)
    print(name)

# f1()
# decorator(f2())

# 多参数,*转换参数为元祖，**转换参数为字典
def f3(func_name):
    print('This is a function3' + func_name)

f3('test func')
f2('test1','test2',a=1,b=2,c='123')