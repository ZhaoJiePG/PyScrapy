# 抓取《我不是药神》的豆瓣评论

import csv
import time
import requests
from lxml import etree

fw = open('douban_comments.csv', 'w')
writer = csv.writer(fw)
writer.writerow(['comment_time','comment_content'])

for i in range(0,20):

    url = 'http://localhost:8050/render.html?url=https://movie.douban.com/subject/26752088/comments?start={}&limit=20&sort=new_score&status=P&timeout=30&wait=0.5'.format(i*20)
    # url = 'https://movie.douban.com/subject/26752088/comments?start={}&limit=20&sort=new_score&status=P'.format(i*20)

    response = requests.get(url)

    tree = etree.HTML(response.text)

    comments = tree.xpath('//div[@class="comment"]')

    for item in comments:
        comment_time = item.xpath('./h3/span[2]/span[contains(@class,"comment-time")]/@title')[0]
        comment_time = int(time.mktime(time.strptime(comment_time,'%Y-%m-%d %H:%M:%S')))
        comment_content = item.xpath('./p/span/text()')[0].strip()
        print(comment_time)
        print(comment_content)
        writer.writerow([comment_time,comment_content])

