# -*- coding: utf-8 -*-
# @Time    : 2022/5/4 22:05
# @Author  : zhuhua
# @File    : financial_ana_data.py
# @Software: PyCharm
import datetime

import pandas as pd


# 数据清洗与读取
# sd.clean_data()


def stock_data_by_time(time=None):
    """
    通过时间导出股票数据
    :param time: str YYYY-mm-dd
    :return: DataFrame
    """
    if time is None:
        time = datetime.datetime.today().date()
    else:
        time = datetime.datetime.strptime(time, '%Y-%m-%d').date()

    cleaned_df = pd.read_csv('..\\resources\\stockBoardEm.csv')
    cleaned_df["ISO时间"] = pd.to_datetime(cleaned_df["ISO时间"])
    cleaned_df = cleaned_df.set_index("ISO时间")
    cleaned_df = cleaned_df.sort_index()
    cleaned_df = cleaned_df[str(time):str(time)].drop_duplicates("股票代码", keep='last')
    return cleaned_df


def stock_data_by_name(name):
    """
    通过名称导出股票数据
    :param name:
    :return:
    """
    cleaned_df = pd.read_csv('..\\resources\\stockBoardEm.csv')
    cleaned_df["ISO时间"] = pd.to_datetime(cleaned_df["ISO时间"])
    cleaned_df["ISO时间"] = cleaned_df["ISO时间"].dt.date
    cleaned_df = cleaned_df[(cleaned_df["股票名称"] == name)].drop_duplicates(["ISO时间"], keep='last')

    return cleaned_df


# print(stock_data_by_time('2022-5-5'))
# print(stock_data_by_name("上海临港"))
# temp_df = stock_data_by_name("上海临港")
# print(temp_df["股票名称"])