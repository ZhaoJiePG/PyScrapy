# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 循环 While
count = 1
while count <= 10:
    count += 1
    print(count)

# 循环 For
a = ['apple', 'orange', 'banabna', 'grape']
for x in a:
    print(x)

a = [['apple', 'orange', 'banabna', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        print(y, end=' ')
else:
    print('fruit is gone')

# 跳出循环
a = [1, 2, 3, 4, 5, 6]
for x in a:
    if x == 2:
        break
    print(x)

for x in range(10, 0, -2):
    print(x, end=' | ')

for x in range(0, len(a), 2):
    print(a[x], end='|')

print(a[0:len(a):2])
