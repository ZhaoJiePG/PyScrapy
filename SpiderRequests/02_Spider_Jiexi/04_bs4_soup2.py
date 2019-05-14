# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

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
soup = BeautifulSoup(html_doc, 'lxml')

# 2.通用解析
# find--返回符合查询条件的 第一个标签
result = soup.find(name='a')
result = soup.find(attrs={'class': 'sister'})
result = soup.find(text='Tillie')
result = soup.find(
    name='p',
    attrs={"class": "story"}
)
print(result)

# find_all
result = soup.find_all(name='a')
result = soup.find_all('a', limit=1)
result = soup.find_all(attrs={'class':'sister'})
print(result)

# select_one--css选择器
result = soup.select_one('.sister')
result = soup.select_one('#one')
result = soup.select_one('#one')
print(result)

# select--css选择器
result = soup.select('.sister')
result = soup.select('#one')
# 父代
result = soup.select('head title')
result = soup.select('title,.title')
# 属性选择器
result = soup.select('a[id="link3"]')
print(result)

# 标签包含的内容--list
result = soup.select('b')[0].get_text()

# 标签的属性
result = soup.select('#link1')[0].get('href')
print(result)
