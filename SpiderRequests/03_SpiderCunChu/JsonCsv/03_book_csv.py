# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json

from lxml import etree
from bs4 import BeautifulSoup
import requests


class BookSpider(object):
    def __init__(self):
        self.base_url = 'http://www.allitebooks.com/page/{}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        self.data_list = []

    # 1.构建所有url
    def get_url_list(self):
        url_list = []
        for i in range(1,5):
          url = self.base_url.format(i)
          url_list.append(url)

        return url_list

    # 2.发请求
    def send_request(self,url):
        data = requests.get(url=url,headers=self.headers).content.decode("gbk")
        print(url)
        return data

    # 3.解析数据
    def prase_xpath_data(self,data):
        prase_data = etree.HTML(data)


        # 1.解析出所有的书
        book_list = prase_data.xpath('//div[@class="main-content-inner clearfix"]/article')

        # 2.解析每本书的信息
        for book in book_list:
            book_dict={}
            # 1.书名
            book_dict['book_name'] = book.xpath('.//h2[@class="entry-title"]/a/text()')[0]

            # 2.书的图片
            book_dict['book_picture'] = book.xpath('./div[@class="entry-thumbnail hover-thumb"]/a/img/@src')[0]

            # 3.书的作者
            book_dict['book_author'] = book.xpath('.//h5[@class="entry-author"]/a/text()')[0]

            # 4.书的简介
            book_dict['book_desc'] = book.xpath('.//div[@class="entry-summary"]/p/text()')[0]

            self.data_list.append(book_dict)

    def prase_bs4_date(self,data):
        # 1.解析出所有的书
        soup = BeautifulSoup(data, 'lxml')
        book_list = soup.select('article')

        # 2.解析每本书的信息
        for book in book_list:
            book_dict={}
            # 1.书名
            book_dict['book_name'] = book.select_one('.main-content-inner clearfix').get_text()

            # 2.书的图片
            book_dict['book_picture'] = book.select_one('.entry-thumbnail hover-thumb').get('src')

            # 3.书的作者
            book_dict['book_author'] = book.select_one('.entry-author').get_text()

            # 4.书的简介
            book_dict['book_desc'] = book.select_one('.entry-summary').get_text()

            self.data_list.append(book_dict)

    # 4.保存数据
    def save_data(self):
        json.dump(self.data_list,open("book.html",'w'))

    # 统筹管理
    def start(self):

        url_list = self.get_url_list()

        # 循环遍历发送请求
        for url in url_list:
            data = self.send_request(url)
            # self.prase_xpath_data(data)
            self.prase_bs4_date(data)
            # self.save_data()

BookSpider().start()