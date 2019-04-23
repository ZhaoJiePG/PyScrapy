# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from Basic.OOP.Extend import People


# from Basic.OOP.Class1 import Student
# 引入外部类
# student = Student("zj", 12)
# student.print_file()

# 继承
class Person(People):
    # 自动继承父类构造器
    def __init__(self, school, name, age):
        self.school = school
        super().__init__(name, age)


person1 = Person("daxue","zj", 1)
print(Person.sum)
print(person1.name)
print(person1.age)
print(person1.school)





