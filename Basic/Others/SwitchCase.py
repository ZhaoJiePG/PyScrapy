# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 用字典代理switchcase
switcher = {
    0 : 'Sunday',
    1 : 'Monday',
    2 : 'Tuesday'
}

day = 6
day_name = switcher.get(day,"Unknow")
print(day_name)

# 函数switch
def get_sunday():
    return 'sunday'

def get_monday():
    return 'Monday'

def get_default():
    return 'Unknow'

switcher = {
    0 : get_sunday(),
    1 : get_monday()
}

day = 6
day_name = switcher.get(day,get_default())
print(day_name)