# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 字典map
dict = {'q':"星月打击", 'w':"苍白之瀑", 'e':"月之降临", 'r':"月神冲刺"}
print(dict)

# 无法存储key相同的
print(dict['q'],dict['r'])

# 多类型,value没有限制，key必须为不可变的类型
dict = {'q':"星月打击", 'w':"苍白之瀑", 'e':"月之降临", 'r':"月神冲刺",q:"aqqw"}

