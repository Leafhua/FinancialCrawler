# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockBoardEm(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    serialNumber = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()
    latestPrice = scrapy.Field()
    quoteChange = scrapy.Field()
    upsAndDowns = scrapy.Field()
    volume = scrapy.Field()
    turnover = scrapy.Field()
    vibration = scrapy.Field()
    turnoverRate = scrapy.Field()
    priceEarningsRatioDynamics = scrapy.Field()
    highest = scrapy.Field()
    lowest = scrapy.Field()
    openToday = scrapy.Field()
    receivedYesterday = scrapy.Field()
    priceToBookRatio = scrapy.Field()
    pass
#http://quote.eastmoney.com/center/boardlist.html#boards-BK06551
