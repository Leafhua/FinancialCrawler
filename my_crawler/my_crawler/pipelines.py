# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from scrapy.utils.project import get_project_settings

settings = get_project_settings()


class MyCrawlerPipeline:

    def __init__(self):
        # 保存本地文件设置
        # self.file = codecs.open('../data/' + datetime.datetime.now().date().isoformat() + '_stockBoardEm.csv', 'w',
        #                         encoding='utf-8-sig')
        # self.fieldnames = ['latestPrice',
        #                    'quoteChange',
        #                    'upsAndDowns',
        #                    'volume',
        #                    'turnover',
        #                    'amplitude',
        #                    'turnoverRate',
        #                    'priceEarningsRatioDynamics',
        #                    'quantityRatio',
        #                    'stockCode',
        #                    'stockName',
        #                    'highest',
        #                    'lowest',
        #                    'openToday',
        #                    'receivedYesterday',
        #                    'priceToBookRatio',
        #                    'ISOdate'
        #                    ]
        # self.csv_writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
        # importlib.reload(sys)

        # 数据库设置
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        self.client = pymongo.MongoClient(host=host, port=port)
        self.mydb = self.client[dbname]

    def open_spider(self, spider):
        if spider.name == 'stockBoardEm':
            # self.csv_writer.writeheader()
            self.sheet = self.mydb[spider.name]

    def process_item(self, item, spider):
        if spider.name == 'stockBoardEm':
            # self.csv_writer.writerow(item)
            self.sheet.insert(dict(item))
        return item

    # def close_spider(self, spider):
    #     if spider.name == 'stockBoardEm':
    #         self.file.close()
