# coding = utf-8

import scrapy


class StockBoardEmSpider(scrapy.Spider):
    name = 'stockBoardEm'
    allowed_domains = ['eastmoney.com']
    # start_urls = ['http://quote.eastmoney.com/stock_list.html']
    start_urls = [
        'http://7.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124034995352995548457_1649165395030&pn=2&pz=20&po=1'
        '&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,'
        'm:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,'
        'f11,f62,f128,f136,f115,f152&_=1649165395151']
    # http://7.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124034995352995548457_1649165395030&pn=2&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1649165395151

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        print('爬取信息：' + response.text)
