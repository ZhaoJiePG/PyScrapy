# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
from threading import Thread


def study():
    print("hello threading")
    time.sleep(2)

if __name__ == '__main__':
    for i in range(5):
        t = Thread(target=study())
        t.start()