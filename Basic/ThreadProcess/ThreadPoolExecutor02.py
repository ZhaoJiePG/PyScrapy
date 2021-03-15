# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Process
import time
import os

def func_1(interval):
    print("funcr_1,父进程(%s),当前进程(%s)"%(os.getppid(),os.getpid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("func_1,执行时间为'%0.2f'秒"%(t_end - t_start))

def  func_2(interval):
    print("func_2,父进程(%s),当前进程(%s)"%(os.getppid(),os.getpid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("func_2,执行时间为'%0.2f'秒"%(t_end - t_start))

p1 = Process(target=func_1,args=(2,))
p2 = Process(target=func_2,name="func2",args=(1,))

# 开启进程
p1.start()
p2.start()

time.sleep(5)
#同时父进程仍然往下执行，如果p2进程还在执行，将会返回True
print("p2.is_alive=%s"%p2.is_alive())
p1.join()
print("p1.is_alive=%s"%p1.is_alive())
