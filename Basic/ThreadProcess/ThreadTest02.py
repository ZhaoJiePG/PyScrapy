# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
from threading import Thread

class Study(Thread):
    def run(self):
        print("study threading....")
        msg = "I am "+self.name+"@"+str(i)
        time.sleep(2)
        print(msg)

if __name__ == '__main__':
    for i in range(5):
        t1 = Study()
        t1.start()