# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from enum import Enum
from enum import IntEnum

class VIP(Enum):
    yello = 1
    green = 2
    black = 3
    red = 4

print(VIP['green'])
print(VIP.green)
# 获取标签名
print(VIP.green.name)
# 获取标签值
print(VIP.green.value)
# 遍历
for v in VIP:
    print(v)
for v in VIP.__members__:
    print(v)

# 枚举转换
class Common():
    YELLOW = 6
a = 6
print(VIP(a))