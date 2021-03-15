# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import time

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))

    return times

executor = ProcessPoolExecutor(max_workers=3)
task1 = executor.submit(get_html(1))
task2 = executor.submit(get_html(2))

#done方法用来判断某个人物是否完成
print(task1.done())
time.sleep(5)
print(task2.done())
print(task1.cancel())
#result方法可以获取task返回值
print(task1.result())