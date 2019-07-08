# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from asyncio import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

option = webdriver.ChromeOptions()
# option.add_argument('headless')

# 要换成适应自己操作系统的chromedriver
driver = webdriver.Chrome(
    executable_path='H:\Pythons\Spider\chromedriver2.exe',
    chrome_options=option
)

url = 'https://www.adidas.com.cn/item/EG1076?locale=zh_CN'

# 打开网站
driver.get(url)

# 打印当前页面标题
print(driver.title)

timeout=5

# 模拟点击“选择尺码”
choose_button = WebDriverWait(driver, timeout).until(
    lambda d: d.find_element_by_xpath('//a[@class="btn"]//span[@class="dropdown-icon"]'))
choose_button.click()

sleep(2)

# 模拟点击“选择尺码”
choose_size = WebDriverWait(driver, timeout).until(
    lambda d: d.find_element_by_xpath('//ul[@class="float-clearfix"]/li[10]/a]'))
print(choose_size)