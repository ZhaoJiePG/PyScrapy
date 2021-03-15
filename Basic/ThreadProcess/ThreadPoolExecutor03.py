# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
multiprocessing.Pool 常用函数解析：

    apply_async(func[, args[, kwds]]) ：非阻塞方式调用 func
    apply(func[, args[, kwds]])：阻塞方式调用 func
    close()：关闭 Process 对象，释放与之关联的所有资源
    terminate()：立即终止进程
    join()：阻塞主进程

'''

from multiprocessing import Pool
import os,time,random

def worker(msg):
    t_start = time.time()
    print("%s START...PROCESS,%d"%(msg,os.getpid()))
    time.sleep(random.random()*10)
    t_stop = time.time()
    print(msg,"END，time：%0.2f"%(t_stop-t_start))

    p=Pool(5) #定义一个进程池，最大进程数5
    for i in range(0,20):
    #每次循环将会用空闲出来的子进程去调用目标
        p.apply_async(worker,(i,))

    p.close() #关闭进程池,不再接收请求
    p.join() #等待p中所有子进程执行完成

worker("task")