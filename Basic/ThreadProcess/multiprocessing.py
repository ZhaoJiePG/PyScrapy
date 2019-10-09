# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 多进程
import os
from multiprocessing import Process

# 获取进程pid
print('Process (%s) start...' % os.getpid())

# 获取父pid
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

def run_proc(name):
    print('Run child process %s(%s)'%(name,os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
