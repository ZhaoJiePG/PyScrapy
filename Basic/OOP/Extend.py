# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
class People():
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sum += 1

    def get_name(self):
        print(self.name)
