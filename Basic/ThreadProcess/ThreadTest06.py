# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import threading
from queue import Queue
from threading import Thread
from time import sleep

'''
semaphore（信号对象）：用于控制进入数量的锁，Semaphore 对象管理着一个计数器，当我们每次调用 acquire() 方法的时候会进行递减，
而每个 release() 方法调用递增，计数器永远不会低于零，当 acquire() 发现计数器为零的时候线程阻塞等待其他线程调用 release()，具体如一下
'''
import threading
import time

#HTML解析线程
class HtmlSpider(threading.Thread):

    def __init__(self,url,sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(1.5)
        print("success get html text,{}".format(self.url))
        self.sem.release()

#URL抓取线程
class UrlGet(threading.Thread):

    def __init__(self,sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            t_html = HtmlSpider("https://www.gitbook.cn/{i}".format(i),self.sem)
            t_html.start()