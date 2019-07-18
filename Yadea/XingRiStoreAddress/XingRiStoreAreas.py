# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
获取新日门店网的所有省市县区县信息
通过请求Ajax接口解析数据
'''
import pandas as pd

from Yadea.XingRiStoreAddress.utils.fileUtils import fileUtils
from Yadea.XingRiStoreAddress.utils.praseUtils import praseUtils
from Yadea.XingRiStoreAddress.utils.requestsUtils import requestsUtils
from Yadea.XingRiStoreAddress.utils.stringUtils import stringUtils


def main():
    # 门店信息ajax接口
    ajaxUrl = 'http://www.xinri.com/Ajax/AjaxHandler_XRDDC.ashx'
    # 解析正则
    regex = r'([\u4e00-\u9fa5]+[a-zA-Z]*\d*[\u4e00-\u9fa5]+\d*[\u4e00-\u9fa5]+)|(\d+\.\d+)'

    # 省参数
    proName = list(fileUtils().getProMiYue('D:\Maven\PyScrapy\Yadea\XingRiStoreAddress\datas\province.csv')[0].keys())[0]
    provinceMiYue = list(fileUtils().getProMiYue('D:\Maven\PyScrapy\Yadea\XingRiStoreAddress\datas\province.csv')[0].values())[0]

    # 获取请求的数据
    data = requestsUtils().getAjaxDatas(ajaxUrl,provinceMiYue)[0]
    print(data)

    # 正则清理数据
    regexList = stringUtils().regex2str(regex,data)
    print(regexList)

    # 保存数据字典并补全省市县
    data = praseUtils().regex2arr(regexList)
    print(data)

    # 补全省市县

    # 保存文件csv格式
    fileUtils().saveAsCsv(data,proName)


if __name__ == '__main__':
    main()