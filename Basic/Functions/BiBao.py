# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
函数式编程   闭包
函数：
    只是一段可执行的代码，不是对象
    另外一个函数的参数，传递到另外一个函数里
'''


# 函数嵌套
# 闭包 = 函数+环境变量(不受外部影响)
def curve_pre():
    a = 25
    def curve(x):
        return a * x * x
    return curve

f = curve_pre()
print(f(2))
print(f.__closure__)
print(f.__closure__[0].cell_contents)
# 柯里化
a = 20
print(curve_pre()(2))

# 闭包必须变量被引用
def f1():
    a = 10
    def f2():
        # 无闭包，此时a被认为是一个局部变量
        # a = 20

        return a
    return f2

f = f1()
print(f)
print(f.__closure__)

# 练习：非闭包
origin = 0
def go(step):
    global origin
    new_pos = origin + step
    origin = new_pos
    return origin

print(go(2))
print(go(3))
print(go(6))

# 练习：闭包，不改变全局变量
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go

tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(6))

