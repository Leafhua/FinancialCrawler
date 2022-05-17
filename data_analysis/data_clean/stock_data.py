# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 17:01
# @Author  : zhuhua
# @File    : stock_data.py
# @Software: PyCharm
import pandas as pd
import pymongo

# DataBase Setting
MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DBNAME = "FinancialCrawler"
MONGODB_SHEETNAME = "stockBoardEm"


def clean_data():
    # 连接数据库
    client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    stock_cur = client[MONGODB_DBNAME][MONGODB_SHEETNAME]

    # 数据清洗
    data = pd.DataFrame(list(stock_cur.find()))
    del data['_id']
    data.columns = [
        "最新价",
        "涨跌幅",
        "涨跌额",
        "成交量",
        "成交额",
        "振幅",
        "换手率",
        "市盈率-动态",
        "量比",
        "股票代码",
        "股票名称",
        "最高",
        "最低",
        "今开",
        "昨收",
        "市净率",
        "ISO时间",
    ]
    data["最新价"] = pd.to_numeric(data["最新价"], errors='coerce')
    data["涨跌幅"] = pd.to_numeric(data["涨跌幅"], errors='coerce')
    data["涨跌额"] = pd.to_numeric(data["涨跌额"], errors='coerce')
    data["成交量"] = pd.to_numeric(data["成交量"], errors='coerce')
    data["成交额"] = pd.to_numeric(data["成交额"], errors='coerce')
    data["振幅"] = pd.to_numeric(data["振幅"], errors='coerce')
    data["换手率"] = pd.to_numeric(data["换手率"], errors='coerce')
    data["市盈率-动态"] = pd.to_numeric(data["市盈率-动态"], errors='coerce')
    data["量比"] = pd.to_numeric(data["量比"], errors='coerce')
    data["股票代码"] = pd.to_numeric(data["股票代码"], errors='coerce')
    data["最高"] = pd.to_numeric(data["最高"], errors='coerce')
    data["最低"] = pd.to_numeric(data["最低"], errors='coerce')
    data["今开"] = pd.to_numeric(data["今开"], errors='coerce')
    data["昨收"] = pd.to_numeric(data["昨收"], errors='coerce')
    data["市净率"] = pd.to_numeric(data["市净率"], errors='coerce')
    data["ISO时间"] = pd.to_datetime(data["ISO时间"], errors='coerce')

    with open('..\\resources\\' + MONGODB_SHEETNAME + '.csv', 'w', encoding='utf-8-sig', newline='') as f:
        data.to_csv(f, index=None)
    print("清洗完成")


# clean_data()

