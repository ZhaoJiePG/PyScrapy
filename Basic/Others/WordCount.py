# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def wordcount(str):
    # 文章字符串前期处理
    strl_ist = str.replace('\n', '').lower().split(' ')
    count_dict = {}
    # 如果字典里有该单词则加1，否则添加入字典
    for str in strl_ist:
        if str in count_dict.keys():
            count_dict[str] = count_dict[str] + 1
        else:
            count_dict[str] = 1
    #按照词频从高到低排列
    # count_list=sorted(count_dict.iteritems(),key=lambda x:x[1],reverse=True)
    return count_dict
