# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import threading
import time

MAX_SIZE = 5
SHARE_Q = []  #模拟共享队列
CONDITION = threading.Condition()

class Producer(threading.Thread):

    def run(self):
        products = range(5)
        global SHARE_Q
        while True:
            # 获取锁
            CONDITION.acquire()
            if len(SHARE_Q) == 5 :
                print("Queue is full...")
                CONDITION.wait()
                print("Consumer have comsumed something")
            # 随机获取产品存入队列
            product = random.choice(products)
            SHARE_Q.append(product)
            print("Producer ：" + str(product))
            CONDITION.notify()
            CONDITION.release()
            time.sleep(1)

class Consumer(threading.Thread):

    def run(self):
        global SHARE_Q
        while True:
            CONDITION.acquire()
            if not SHARE_Q :
                print("Queue is Empty...")
                CONDITION.wait()
                print("Producer have producted something")
            product = SHARE_Q.pop(0)
            print("Consumer :", product)
            CONDITION.notify()
            CONDITION.release()
            time.sleep(random.random())

if __name__ == '__main__':
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()