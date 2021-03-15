# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import threading
from queue import Queue
from threading import Thread
from time import sleep

'''
线程同步：condition、Semaphore 使用

condition（条件变量）：condition 有两把锁，一把底层锁会在线程底层调用 wait 后释放。我们每次调用 wait 时候回分配一把锁放到 condition 的等待队列中等待 notify 方法的唤醒。
'''

class factory(Thread):

    def __init__(self,cond):
        super(factory,self).__init__(name="口罩生产厂家")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}:生产了10万个口罩，快来拿".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:又生产了100万个口罩发往武汉".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:加油，武汉！".format(self.name))
            self.cond.notify()

class wuhan(Thread):
    def __init__(self,cond):
        super(wuhan,self).__init__(name="武汉志愿者")
        self.cond = cond

    def run(self):
        with self.cond:

            print("{}:能帮我们生产一批口罩吗？".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}:谢谢你们".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}:一起加油".format(self.name))
            self.cond.notify()
            self.cond.wait()

if __name__=="__main__":
    lock = threading.Condition()
    factory = factory(lock)
    wuhan = wuhan(lock)
    factory.start()
    wuhan.start()