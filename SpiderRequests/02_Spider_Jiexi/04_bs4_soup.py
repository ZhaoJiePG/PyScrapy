# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import  BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">...</p>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 1.转换类型
# 默认bs4会 调用系统中的lxml的解析库 警告提示
# 主动设置 bs4的解析库,BeautifulSoup对象
soup = BeautifulSoup(html_doc,'lxml')
print(type(soup))

# 2.格式化输出 补全
result = soup.prettify()
print(result)

# 3.解析数据
# Tag标签对象
head = soup.head
print(type(head))
p = soup.p
p = soup.p.string
print(p)
# 注释的内容是comment类型
print(type(p))

a = soup.a
print(a)

# 取内容NavigableString
result = soup.a.string
print(type(result))
print(result)

# 取属性
result = soup.a.href
print(result)
