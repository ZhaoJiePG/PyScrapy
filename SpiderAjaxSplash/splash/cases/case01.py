# 抓取今日头条，对比渲染和没有渲染的效果

import requests
from lxml import etree

# url = 'http://localhost:8050/render.html?url=https://www.toutiao.com&timeout=30&wait=0.5'
url = 'https://www.toutiao.com'

response = requests.get(url)

print(response.text)

tree = etree.HTML(response.text)

article_titles = tree.xpath('//div[@class="title-box"]/a/text()')

print(article_titles)