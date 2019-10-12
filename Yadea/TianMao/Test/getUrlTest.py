# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# search_name='%D1%C5%B5%CF%B5%E7%B6%AF%B3%B5'
import json
import re

import requests

from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 请求url
# search_name = '雅迪电动车'
# url = 'https://list.tmall.com/search_product.htm?q={0}&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton'.format(search_name)
# print(url)
#
# # 响应
# response = requests.get(url)
# print(response.text)
#
# context = response.text
#
# # 解析
# selector = etree.HTML(context)
# name = selector.xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div/p[1]/text()')
# date = selector.xpath('/html/body/div[1]/div[2]/div[1]/div/div[3]/div[2]/ul/table/tbody/tr[1]/td[1]/text()')
# price = selector.xpath('/html/body/div[1]/div[2]/div[1]/div/div[3]/div[2]/ul/table/tbody/tr[1]/td[3]/text()')
# price = (str(price[0]).replace('\n','').replace('\r','').replace(' ',''))


search_name = '雅迪电动车'
ref_url = 'https://detail.tmall.com/item.htm?id=589515074188&skuId=4197620318903&user_id=2200728804162&cat_id=2&is_b=1&rn=42665760fcead2c829a10fd40c73ef73'

url = 'https://rate.tmall.com/list_detail_rate.htm?' \
      'itemId=596624138584&' \
      'spuId=1243962245&' \
      'sellerId=2817130358&' \
      'order=3&' \
      'currentPage=10&'
print(url)

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": "cna=L0CwFSqRDGgCAd9EwPN4s9v5; t=3f886137b6f604509bea316d5773e8af; _tb_token_=33135eebeb15b; cookie2=1b0b4e285c2d20c244c712d49635efa6; dnk=%5Cu767D%5Cu767D%5Cu7684%5Cu72D7%5Cu5C3E%5Cu5DF4%5Cu82B1; uc1=pas=0&lng=zh_CN&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie21=URm48syIYn73&existShop=false&tag=8&cookie14=UoTbnV%2BOqCmL2A%3D%3D; uc3=id2=UUpjN4zrNdJETg%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&vt3=F8dByuDnzROHAQ3X%2FeU%3D&nk2=05emRgpWdtZcceNuDGg%3D; tracknick=%5Cu767D%5Cu767D%5Cu7684%5Cu72D7%5Cu5C3E%5Cu5DF4%5Cu82B1; lid=%E7%99%BD%E7%99%BD%E7%9A%84%E7%8B%97%E5%B0%BE%E5%B7%B4%E8%8A%B1; uc4=nk4=0%400SwjusWimre0H6WrAcFT6cSTu0IPkewtmQ%3D%3D&id4=0%40U2gp9xkNePhwkA3mujHlbSd34BVR; _l_g_=Ug%3D%3D; unb=2221579274; lgc=%5Cu767D%5Cu767D%5Cu7684%5Cu72D7%5Cu5C3E%5Cu5DF4%5Cu82B1; cookie1=VWsu%2BpKF9hE9HePBZc%2FExBxRmsDaR97K6DS4nKh4iu0%3D; login=true; cookie17=UUpjN4zrNdJETg%3D%3D; _nk_=%5Cu767D%5Cu767D%5Cu7684%5Cu72D7%5Cu5C3E%5Cu5DF4%5Cu82B1; sg=%E8%8A%B145; csg=029a3cd0; enc=x%2BbRQuO%2FU%2FgQU1XAlsZpeiOZ1IHkZYtObQTBaOQawfBHOzzdocAvLvbm28eF8EIDr9V4tZaW0jnMGkmhRNm10g%3D%3D; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; whl=-1%260%260%260; x=__ll%3D-1%26_ato%3D0; l=cBSH0T-4q4bTAKD8BOCgCZMInnbO9LAfguWXRJ8ei_5ZZsTVpQbOkiBbsU96cjWFTw8B4nnADjetjecb-yWfoTB7K9cdvdC..; isg=BHV1MEyeRJRSkKAV4I7I9ewrkfElZ3NQbmaCt_eaDOx4zpTAv0Nq1eSIGNLdjkG8",
    "referer": "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.11.7b287e09a2f8pU&id=596624138584&skuId=4315669582772&areaId=320200&user_id=2817130358&cat_id=2&is_b=1&rn=8630e2eec4c15b75a52ce788af26c28b",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3732.400 QQBrowser/10.5.3819.400"}

# 响应
response = requests.get(url, headers=headers)
data = response.text
re_data = re.findall('{.*}', data)[0]
print(re_data)

json_date = json.loads(re_data)['rateDetail']['rateList']

# 评论list
rate_list = []
for rate in json_date:
    rateDate = rate['rateDate']
    rateContent = rate['rateContent']
    auctionSku = rate['auctionSku']
    cmsSource = rate['cmsSource']
    rate_list.append({'rateDate':rateDate,'rateContent':rateContent,'auctionSku':auctionSku,'cmsSource':cmsSource})
    print(rateContent)
# print(rate_list)
