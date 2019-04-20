# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Test():
    def __bool__(self):
        return True
    def __len__(self):
        return 0

print(bool(Test()))