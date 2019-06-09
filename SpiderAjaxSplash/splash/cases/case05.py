# python执行一段更加复杂的lua脚本
# 抓取京东商品信息

import json
import requests
from lxml import etree
from urllib.parse import quote

lua = '''
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("https://search.jd.com/Search?keyword=相机&enc=utf-8")
        return {
            html = treat.as_string(response.body),
            url = response.url,
            status = response.status
        }    
end
'''

# 线上部署的服务，需要将localhost换成服务器的公网地址（不是内网地址）
url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)

html = json.loads(response.text)['html']

tree = etree.HTML(html)

# 单品
products_1 = tree.xpath('//div[@class="gl-i-wrap"]')

for item in products_1:
    try:
        name_1 = item.xpath('./div[@class="p-name p-name-type-2"]/a/em/text()')[0]
        price_1 = item.xpath('./div[@class="p-price"]/strong/@data-price | ./div[@class="p-price"]/strong/i/text()')[0]
        print(name_1)
        print(price_1)
    except:
        pass

# 套装
products_2 = tree.xpath('//div[@class="tab-content-item tab-cnt-i-selected"]')

for item in products_2:
    name_2 = item.xpath('./div[@class="p-name p-name-type-2"]/a/em/text()')[0]
    price_2 = item.xpath('./div[@class="p-price"]/strong/@data-price | ./div[@class="p-price"]/strong/i/text()')[0]
    print(name_2)
    print(price_2)