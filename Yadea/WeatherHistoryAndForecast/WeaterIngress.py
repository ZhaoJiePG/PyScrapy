# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-


'''
历史天气：http://www.tianqihoubao.com/lishi/
天气预报：http://www.tianqi.com/rizhao/30/

爬取思路：
1.获取第一面的所有城市和区县，保存本地
2.根据获取的省市县查询昨天之前历史每天天气，日期为外部字典表，保存本地
3.爬取昨天的天气，保存本地
4.保存爬取数据到mysql
'''
from lxml import etree
from Yadea.WeatherHistoryAndForecast.fileUtils import fileUtils
from Yadea.WeatherHistoryAndForecast.mysqlUtils import querySql
from Yadea.WeatherHistoryAndForecast.requestsUtils import requestsUtils
from Yadea.WeatherHistoryAndForecast.stringUtils import stringUtils

# 获取第一面的所有城市和区县，保存本地
def getProvinceCity():
    # 1.请求url
    # url = 'http://www.tianqihoubao.com/lishi/'
    f = open('./Datas/ProvinceCityInfo/url.txt', 'rb')
    data = f.read().decode('utf-8')
    xpathData = etree.HTML(data)
    # 2.获取省的div
    provinceList = xpathData.xpath('//div[@class="citychk"]/dl')
    # 省市集合
    provinceCityList = []
    for provinceCityData in provinceList:
        # 3.获取省
        provinceName = provinceCityData.xpath('./dt/a/b/text()')[0]
        # print(provinceName)
        # 4.获取市
        for cityList in provinceCityData.xpath('./dd/a'):
            cityName = cityList.xpath('./text()')[0].replace(' ', '')
            cityPinYin = stringUtils().string2Pinyin(cityName)
            provinceCityList.append({'provinceName': provinceName, 'cityName': cityName, 'cityPinYin': cityPinYin})
    # print(provinceCityList)
    fileUtils().saveAsCsv(provinceCityList, 'ProvinceCityInfo/ProvinceCity')

# 获取各个城市的历史天气情况
def getWeatherHistory():
    # 获取爬取的城市(本地获取)
    provinceCityList = fileUtils().getCsvFile('./Datas/ProvinceCityInfo/ProvinceCity.csv')
    print(provinceCityList)
    # 获取爬取的年月(数据库查询)
    sql = """
        select 
            distinct month_id
        from 
            spider.dm_dim_day
        where
            day_short_desc = '2019-01-01';
        """
    dateDict = querySql(sql)
    dateList = [monthId['month_id'] for monthId in dateDict]
    yearName = dateList[0]
    print(yearName)
    # print(dateList)
    # 天气信息集合
    weatherList = []
    for dateIndex in dateList:
        for i in range(1, 287):
            # 获取省市名称
            provinceName = provinceCityList[i][2]
            cityName = provinceCityList[i][0]
            cityPinYin = provinceCityList[i][1]
            print("开始爬取=="+str(i)+":"+provinceName+":"+cityName+":"+dateIndex+"==的历史天气信息")
            # 请求城市天气url
            url = 'http://www.tianqihoubao.com/lishi/{0}/month/{1}.html'.format(cityPinYin,dateIndex)
            # print(url)
            urlData = requestsUtils().getUrl(url)  ##.replace('\n','').replace('\r','').replace(' ','')
            xpathData = etree.HTML(urlData)
            # 获取天气信息
            weatherTable = xpathData.xpath('//table[@class="b"]/tr')
            for index in range(2, len(weatherTable) + 1):
                # 日期
                weatherDate = xpathData.xpath('//table[@class="b"]/tr[{0}]/td[1]/a/text()'.format(index))[0] \
                    .replace('\n','').replace('\r','').replace(' ','') \
                    .replace('日','').replace('年','-').replace('月','-')
                # 天气状态
                weatherStatus = xpathData.xpath('//table[@class="b"]/tr[{0}]/td[2]/text()'.format(index))[0] \
                    .replace('\n','').replace('\r','').replace(' ','')
                # 温度
                weatherTemperature = xpathData.xpath('//table[@class="b"]/tr[{0}]/td[3]/text()'.format(index))[0] \
                    .replace('\n','').replace('\r','').replace(' ','')
                # 风速
                weatherWind = xpathData.xpath('//table[@class="b"]/tr[{0}]/td[4]/text()'.format(index))[0] \
                    .replace('\n','').replace('\r','').replace(' ','')
                weatherDict = {'provinceName':provinceName,'cityName':cityName,'weatherDate':weatherDate,'weatherStatus':weatherStatus,'weatherTemperature':weatherTemperature,'weatherWind':weatherWind}
                print(weatherDict)
                weatherList.append(weatherDict)
    fileUtils().saveAsCsv(weatherList,'Weathers/{}'.format(yearName))
if __name__ == '__main__':
# # 1.获取需要爬取的省市位置
# # getProvinceCity()
# # 2.获取详细城市的历史天气情况
    getWeatherHistory()
