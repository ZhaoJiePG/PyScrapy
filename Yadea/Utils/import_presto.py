# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd

tb_pro = pd.read_csv('province.csv')
tb_city = pd.read_csv('city.csv')

join = pd.merge(tb_pro,tb_city,on="key")
result = pd.DataFrame(join)
result.to_csv('result.csv',header=True,index=False)

print(result)