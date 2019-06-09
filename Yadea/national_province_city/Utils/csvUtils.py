# Author:Aliex ZJ
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import csv

import pandas as pd


def import_csv(data, name, path):
    df = pd.DataFrame(data)
    res_path = path + name + '.csv'
    df.to_csv(res_path, sep=',', header=True, index=False,encoding='utf-8')
    print("写入文件" + res_path + "成功")
    return df


def get_csv(path, name,column):
    csv = pd.read_csv(path + name + '.csv',encoding='utf-8')
    return csv[column]


def sort_csv(data,column):
    df_data = pd.DataFrame(data).sort_values(by = [column])
    return df_data


def get_df(path, name):
    csv = pd.read_csv(path + name + '.csv',encoding='utf-8')
    return csv



