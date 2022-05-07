# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 23:33
# @Author  : zhuhua
# @File    : test.py
# @Software: PyCharm
import financial_ana_data

time_df = financial_ana_data.stock_data_by_time("2022-5-6")

# list1 = time_df[["股票名称", "昨收"]].values.tolist()
time_df = time_df.dropna(subset=["昨收"])
list2 = time_df.sort_values(by="昨收", ascending=False)[["股票名称", "昨收"]].head(500).values.tolist()
print(list2)

