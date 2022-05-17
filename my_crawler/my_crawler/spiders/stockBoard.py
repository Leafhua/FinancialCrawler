# coding = utf-8
import datetime
import json

import pandas as pd
import scrapy

from ..items import StockBoardEmItem


class StockBoardEmSpider(scrapy.Spider):
    name = 'stockBoardEm'
    allowed_domains = ['eastmoney.com']

    # 东方财经网api
    start_urls = ['http://34.push2.eastmoney.com/api/qt/clist/get?&pn=1&pz=5000&po=1&np=1&ut'
                  '=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,'
                  'm:0+t:81+s:2048&fields=f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f14,f15,f16,f17,f18,f23'
                  '&_=1650124477218']

    # http://34.push2.eastmoney.com/api/qt/clist/get?&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1650124477218
    # f2最新价 f3涨跌幅 f4涨跌额 f5成交量 f6成交额 f7振幅 f8换手率 f9市盈率-动态 f10量比 f12股票代码 f14股票名称 f15最高 f16最低 f17今开 f18昨收 f23市净率

    def parse(self, response):
        data_json = json.loads(response.text)
        temp_df = pd.DataFrame(data_json['data']['diff'])

        for index, row in temp_df.iterrows():
            item = StockBoardEmItem()
            item['latestPrice'] = row[0]
            item['quoteChange'] = row[1]
            item['upsAndDowns'] = row[2]
            item['volume'] = row[3]
            item['turnover'] = row[4]
            item['amplitude'] = row[5]
            item['turnoverRate'] = row[6]
            item['priceEarningsRatioDynamics'] = row[7]
            item['quantityRatio'] = row[8]
            item['stockCode'] = row[9]
            item['stockName'] = row[10]
            item['highest'] = row[11]
            item['lowest'] = row[12]
            item['openToday'] = row[13]
            item['receivedYesterday'] = row[14]
            item['priceToBookRatio'] = row[15]
            item['ISOdate'] = datetime.datetime.now().replace(microsecond=0).isoformat()
            # print(item)
            # print(row)
            # break
            yield item

