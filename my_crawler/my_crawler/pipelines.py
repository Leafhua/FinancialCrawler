# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import codecs
import csv
import datetime
import importlib
import sys


class MyCrawlerPipeline:

    def __init__(self):
        self.file = codecs.open('../data/' + datetime.datetime.now().date().isoformat() + '_stockBoardEm.csv', 'w',
                                encoding='utf-8-sig')
        self.fieldnames = ['latestPrice',
                           'quoteChange',
                           'upsAndDowns',
                           'volume',
                           'turnover',
                           'amplitude',
                           'turnoverRate',
                           'priceEarningsRatioDynamics',
                           'quantityRatio',
                           'stockCode',
                           'stockName',
                           'highest',
                           'lowest',
                           'openToday',
                           'receivedYesterday',
                           'priceToBookRatio',
                           ]
        self.csv_writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
        importlib.reload(sys)

    def open_spider(self, spider):
        if spider.name == 'stockBoardEm':
            self.csv_writer.writeheader()

    def process_item(self, item, spider):
        if spider.name == 'stockBoardEm':
            self.csv_writer.writerow(item)
        return item

    def close_spider(self, spider):
        if spider.name == 'stockBoardEm':
            self.file.close()
