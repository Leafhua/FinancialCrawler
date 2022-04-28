# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockBoardEmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 股票代码
    stockCode = scrapy.Field()
    # 股票名称
    stockName = scrapy.Field()
    # 今开
    openToday = scrapy.Field()
    # 昨收
    receivedYesterday = scrapy.Field()
    # 最新价
    latestPrice = scrapy.Field()
    # 最高
    highest = scrapy.Field()
    # 最低
    lowest = scrapy.Field()
    # 涨跌幅
    quoteChange = scrapy.Field()
    # 涨跌额
    upsAndDowns = scrapy.Field()
    # 振幅
    amplitude = scrapy.Field()
    # 市盈率-动态
    priceEarningsRatioDynamics = scrapy.Field()
    # 量比
    quantityRatio = scrapy.Field()
    # 换手率
    turnoverRate = scrapy.Field()
    # 市净率
    priceToBookRatio = scrapy.Field()
    # 成交量
    volume = scrapy.Field()
    # 成交额
    turnover = scrapy.Field()
    pass
# http://quote.eastmoney.com/center/boardlist.html#boards-BK06551
