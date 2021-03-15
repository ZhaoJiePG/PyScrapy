# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from threading import Thread
from time import sleep

nums = 100

def setNums():
    global nums
    for i in range(5):
        nums +=1

    print("in setNums nums is %d"%nums)

def getNums():

    print("in getNums nums is %d"%nums)

print("线程创建之前:%d"%nums)

t1 = Thread(target=setNums)
t1.start()

sleep(3)

t2 = Thread(target=getNums)
t2.start()