# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from queue import Queue
from threading import Thread
from time import sleep


#生产者
def Producer():
    count =0
    while True:
        if queue.qsize()<1000:
            for i in range(100):
                count +=1
                msg = "生产商品"+str(count)
                queue.put(msg)
                print(msg)

        sleep(0.5)

#消费者
def Consumer():
    while True:
        if queue.qsize()>100:
            for i in range(3):
                msg = "消费者消费了"+queue.get()
                print(msg)

        sleep(1)

if __name__=="__main__":
    #定义一个队列
    queue = Queue()

    #初始化商品
    for i in range(500):
        queue.put("初始商品"+str(i))
        #生产商品
        for i in range(4):
            p = Thread(target=Producer)
            p.start()
        #消费商品
        for i in range(10):
            c = Thread(target=Consumer)
            c.start()