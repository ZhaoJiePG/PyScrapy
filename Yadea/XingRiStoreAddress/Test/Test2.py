# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

url = 'http://www.bejson.com/convert/unicode_chinese/'

# 打开网站
driver.get(url)

context = driver.find_element_by_xpath('//*[@id="json_input"]')
print(context)
# driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/form/div[1]/div[6]/div[1]/div/div/div/div[5]/div/pre/span')\
context.send_keys('%3Cdl%20class%3D%22cf%22%20data-title%3D%22%u5317%u4EAC%u987A%u8FBE%u8DEF%u901A%u5546%u8D38%u6709%u9650%u516C%u53F8%22%20data-point%3D%22116.196964%')
a = context.send_keys(Keys.RETURN)
print(a)

driver.find_element_by_xpath('//*[@id="JSONVYasuo"]/div[2]/div/input[1]').click()

# 复制
context.send_keys(Keys.CONTROL,'a')
context.send_keys(Keys.CONTROL,'c')

driver.close()
