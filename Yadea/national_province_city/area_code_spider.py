# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 省级别信息获取

from Yadea.national_province_city.Prases.getCity import getCity
from Yadea.national_province_city.Prases.getCounty import getCounty
from Yadea.national_province_city.Prases.getProvince import getProvince
from Yadea.national_province_city.Prases.getTown import getTown
from Yadea.national_province_city.Prases.getVillage import getVillage
from Yadea.national_province_city.Utils.csvUtils import import_csv, get_csv


def main(base_url,data_path):
    # 获取省信息
    # province = getProvince(base_url)
    # # 保存省信息
    # import_csv(province,'province',data_path)

    # 获取省的url
    # province_url = get_csv(data_path,'province','link')
    # # 获取市信息
    # city = getCity(province_url)
    # # 保存市信息
    # import_csv(city,'city',data_path)

    # # 获取市的url
    # province_url = get_csv(data_path,'city','link')
    # # 获取区信息
    # county = getCounty(province_url)
    # # 排序
    # df_county = sort_csv(county,'code')
    # # 保存区信息
    # import_csv(df_county,'county',data_path)
    #
    # # 获取区的url
    # county_url = get_csv(data_path,'county','link')
    # # 获取乡镇信息
    # town = getTown(county_url)
    # # 保存乡镇信息
    # import_csv(town,'town',data_path)

    #获取的乡镇url

    # 获取街道信息
    town_url = get_csv(data_path,'town','link')
    village = getVillage(town_url)
    # 保存街道信息
    import_csv(village,'village',data_path)


    # 存入mysql
    # df = get_df(data_path,'province')
    # csv2mysql('test','spider_province',df)
    #
    # df = get_df(data_path,'city')
    # csv2mysql('test','spider_city',df)
    #
    # df = get_df(data_path,'county')
    # csv2mysql('test','spider_county',df)
    #
    # df = get_df(data_path,'town')
    # csv2mysql('test','spider_town',df)
    #
    # df = get_df(data_path,'village')
    # csv2mysql('test','spider_village',df)

if __name__ == '__main__':
    # 初始url
    base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html'
    # 数据保存路径
    data_path= 'H:\\Pythons\\PyData\\PyScrapy\\Yadea\\national_province_city\\data\\'
    main(base_url,data_path)