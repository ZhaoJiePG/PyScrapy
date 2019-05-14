# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

# 匹配中文,unicode范围
str = '''
<area style="cursor:pointer;outline:none;" shape="rect" coords="0,0,270,129" href="//www.baidu.com/s?wd=%E4%BB%8A%E6%97%A5%E6%96%B0%E9%B2%9C%E4%BA%8B&amp;tn=SE_Pclogo_6ysd4c7a&amp;sa=ire_dl_gh_logo&amp;rsv_dl=igh_logo_pc" target="_blank" title="点击一下，了解更多" onmousedown="return ns_c({'fm':'behs','tab':'bdlogo'})">
'''

pattern = re.compile('[\u4e00-\u9fa5]+')
res = pattern.findall(str)
print(res)
