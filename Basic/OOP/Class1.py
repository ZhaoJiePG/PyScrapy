# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 面向对象,封装
class Student():
    # 特征,类变量相当于静态变量
    sum = 0
    name = ''
    age = 0

    # 类变量，实例变量

    # 构造函数，构造器,实例化的时候自动调用，无返回值
    def __init__(self, name, age):
        # 初始化对象属性
        self.name = name
        self.age = age
        self.score = 0
        # print("student")
        # 访问类变量
        # self.__class__.sum += 1
        # print("当前人数"+str(self.__class__.sum))

    # 实例方法必须要self
    # 行为
    def do_homeword(self):
        pass

    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

    # 定义类方法：加装饰器
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    # 定义静态方法：加装饰器
    @staticmethod
    def add(x, y):
        print('This is static method')
        # 访问实例变量
        print(sum)
        # 访问类方法

    def marking(self, score):
        if score < 0:
            return '不可以给别人打负分'
        self.score = score
        print(self.name + '同学成绩为' + str(self.score))


# 实例化
student1 = Student("zj", 12)
student2 = Student("zj1", 12)
print(Student.plus_sum())
# 所有隐藏的变量
print(student1.__dict__)
print(student1.name)

# 访问类变量
print(Student.name)
# 对象调用类方法
print(student1.plus_sum())

# 调用静态方法
print(Student.add(1, 2))
print(student1.add(1, 2))


# student2 = Student()
# print(student2.print_file())
# student3 = Student()
# print(student3.print_file())
#
# print(id(student1))
# print(id(student2))
# print(id(student3))

# 行为
# class Priter():
#     def print_file(self):
#         print('name:' + self.name)
#         print('age:' + str(self.age))

class StudentHomework():
    homework_name = ''
