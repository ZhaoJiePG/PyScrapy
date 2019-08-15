# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from urllib3.util import timeout

option = webdriver.ChromeOptions()
# option.add_argument('headless')

# 要换成适应自己操作系统的chromedriver
driver = webdriver.Chrome(
    executable_path='D:\Maven\PyScrapy\SpiderHeaderless\chromedriver.exe',
    chrome_options=option
)

url = 'http://www.xinri.com/service/internet.html'

# 打开网站
driver.get(url)
driver.implicitly_wait(2)
# 选择省下拉框
ele = driver.find_element_by_id("province")
Select(ele).select_by_value("江苏省")
# 选择市下拉框
ele = driver.find_element_by_id("city")
Select(ele).select_by_value("无锡市")
# 选择县下拉框
ele = driver.find_element_by_id("district")
Select(ele).select_by_value("锡山区")
driver.implicitly_wait(1)
# 点击搜索框
serachButton = driver.find_element_by_id("butinternet")
serachButton.click()
driver.implicitly_wait(2)
div = driver.find_element_by_css_selector('div.cf>div')
print(div.id)
print(div.text)
print(div.get_property('class'))
# driver.close()
