from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
# option.add_argument('headless')

driver = webdriver.Chrome(
    executable_path='D:\Maven\PyScrapy\SpiderHeaderless\chromedriver.exe',
    chrome_options=option
)

url = 'https://detail.tmall.com/item.htm?id=589515074188&skuId=4197620318903&user_id=2200728804162&cat_id=2&is_b=1&rn=9a78753a84b6d08e0a2ba874ccbe9cee'
driver.get(url)
print(driver.title)

timeout = 5

# 点击关闭登陆按钮
close_sign_button = driver.find_element_by_xpath('//*[@id="J_TabBar"]/li[2]/a')
print(close_sign_button)
close_sign_button.click()