# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re


class stringUtils():
    def __init__(self):
        pass

    # 字符串%unicode解码中文
    def unicode2str(self,str):
        res = eval(repr(str.replace('%u', '\\u')).replace('\\\\','\\')).encode('unicode_escape').decode('unicode_escape')
        # 过滤北京
        resBeiJing = res.replace('%28', '').replace('(', '').replace(')', '').replace(' ', '').replace('（', '').replace('）', '').replace('-', '').replace('%20','').replace('A','').replace('姜海燕','').replace('、','')
        # 过滤天津
        resTianJing = resBeiJing.replace('%0','').replace('：','')
        return (resBeiJing,resTianJing)


    # 正则解析
    def regex2str(self,regex,str):
        # res = re.findall(regex,str)
        pattern = re.compile(regex)
        res = pattern.findall(str)
        return res


# str = "{state: 1,info: '%3Cdl%20class%3D%22cf%22%20data-title%3D%22%u5317%u4EAC%u987A%u8FBE%u8DEF%u901A%u5546%u8D38%u6709%u9650%u516C%u53F8%22%20data-point%3D%22116.196964%2C39.928473%22%20data-address%3D%22%u5317%u4EAC%u77F3%u666F%u5C71%u533A%u6768%u5E84%u4E1C%u885721%u53F7%22%20data-tel%3D%2218911667657%22%3E%0D%0A%3Cdt%20class%3D%22fl%22%3E01%3C/dt%3E%0D%0A%3Cdd%20class%3D%22of%22%3E%0D%0A%3Ch3%20class%3D%22font-20%22%3E%u5317%u4EAC%u987A%u8FBE%u8DEF%u901A%u5546%u8D38%u6709%u9650%u516C%u53F8%3C/h3%3E%0D%0A%3Cp%3E%u5317%u4EAC%u77F3%u666F%u5C71%u533A%u6768%u5E84%u4E1C%u885721%u53F7%3C/p%3E%0D%0A%3Cp%20class%3D%22t%22%3E%3Cimg%20src%3D%22/images/int_1.png%22%20/%3E18911667657%3C/p%3E%0D%0A%3C/dd%3E%0D%0A%3C/dl%3E%0D%0A%3Cdl%20class%3D%22cf%22%20data-title%3D%22%u5317%u4EAC%u946B%u6CF0%u5229%u53D1%u5546%u8D38%u6709%u9650%u516C%u53F8%28%u76F4%u8425%29%22%20data-point%3D%22116.186923%2C39.914813%22%20data-address%3D%22%u5317%u4EAC%u77F3%u666F%u5C71%u533A%u53E4%u57CE%u5927%u88576%u53F7%22%20data-tel%3D%2213521556028%22%3E%0D%0A%3Cdt%20class%3D%22fl%22%3E02%3C/dt%3E%0D%0A%3Cdd%20class%3D%22of%22%3E%0D%0A%3Ch3%20class%3D%22font-20%22%3E%u5317%u4EAC%u946B%u6CF0%u5229%u53D1%u5546%u8D38%u6709%u9650%u516C%u53F8%28%u76F4%u8425%29%3C/h3%3E%0D%0A%3Cp%3E%u5317%u4EAC%u77F3%u666F%u5C71%u533A%u53E4%u57CE%u5927%u88576%u53F7%3C/p%3E%0D%0A%3Cp%20class%3D%22t%22%3E%3Cimg%20src%3D%22/images/int_1.png%22%20/%3E13521556028%3C/p%3E%0D%0A%3C/dd%3E%0D%0A%3C/dl%3E%0D%0A%3Cdl%20class%3D%22cf%22%20data-title%3D%22%u5317%u4EAC%u5357%u5C71%u98DE%u9E3F%u5546%u8D38%u6709%u9650%u516C%u53F8%22%20data-point%3D%22116.18239%2C39.907839%22%20data-address%3D%22%u5317%u4EAC%u5E02%u77F3%u666F%u5C71%u533A%u8001%u53E4%u57CE%u5927%u697C9%u53F7%u697C%u5E95%u55461%u53F7%22%20data-tel%3D%2215010871814%22%3E%0D%0A%3Cdt%20class%3D%22fl%22%3E03%3C/dt%3E%0D%0A%3Cdd%20class%3D%22of%22%3E%0D%0A%3Ch3%20class%3D%22font-20%22%3E%u5317%u4EAC%u5357%u5C71%u98DE%u9E3F%u5546%u8D38%u6709%u9650%u516C%u53F8%3C/h3%3E%0D%0A%3Cp%3E%u5317%u4EAC%u5E02%u77F3%u666F%u5C71%u533A%u8001%u53E4%u57CE%u5927%u697C9%u53F7%u697C%u5E95%u55461%u53F7%3C/p%3E%0D%0A%3Cp%20class%3D%22t%22%3E%3Cimg%20src%3D%22/images/int_1.png%22%20/%3E15010871814%3C/p%3E%0D%0A%3C/dd%3E%0D%0A%3C/dl%3E%0D%0A%3Cdl%20class%3D%22cf%22%20data-title%3D%22%u9C81%u8C37%u8DEF%u65B0%u65E5%22%20data-point%3D%22116.22117742896081%2C39.89958116009062%22%20data-address%3D%22%u9C81%u8C37%u8857%u9053%22%20data-tel%3D%2213391731168%22%3E%0D%0A%3Cdt%20class%3D%22fl%22%3E04%3C/dt%3E%0D%0A%3Cdd%20class%3D%22of%22%3E%0D%0A%3Ch3%20class%3D%22font-20%22%3E%u9C81%u8C37%u8DEF%u65B0%u65E5%3C/h3%3E%0D%0A%3Cp%3E%u9C81%u8C37%u8857%u9053%3C/p%3E%0D%0A%3Cp%20class%3D%22t%22%3E%3Cimg%20src%3D%22/images/int_1.png%22%20/%3E13391731168%3C/p%3E%0D%0A%3C/dd%3E%0D%0A%3C/dl%3E%0D%0A'}"
# res = stringUtils().unicode2str(str)
#
# print(res)
#
# # 解析地理位置信息
# # regex = '([\\u4e00-\\u9fa5]+).*22' \
# #         '([0-9]+\.[0-9]+)%2C'+'([0-9]+\.[0-9]+)' \
# #         # '.*22([\\u4e00-\\u9fa5]+[0-9]{1,4}[\\u4e00-\\u9fa5]+)'\
# #         # '%22%20data-tel%3D%22([0-9]+)'
#
# regex = '([\u4e00-\u9fa5]{3,}\d*[\u4e00-\u9fa5])|(\d+\.\d+)|(\d{12,})'
#
# res = re.findall(regex,res)
# print(res)
