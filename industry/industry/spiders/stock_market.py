from selenium.webdriver import Chrome

import scrapy

from industry.items import StockMarketItem


class StockMarketSpider(scrapy.Spider):
    '''
    大盘行情（沪市，深市，创业板）
    '''
    name = 'stock_market'
    start_urls = [
        'http://quote.eastmoney.com/zs000001.html',  # 沪市
        'http://quote.eastmoney.com/zs399001.html',  # 深圳
        'http://quote.eastmoney.com/zs399006.html'  # 创业板

    ]

    def __init__(self, *args, **kwargs):
        self.bro = Chrome()

    def parse(self, response):
        print(response)
        # 大盘指数
        item = StockMarketItem()

        item['market_name'] = response.xpath('//*[@id="name"]/text()').extract_first()
        item['market_code'] = response.xpath('//*[@id="code"]/text()').extract_first()
        item['open'] = response.xpath('//*[@id="rgt2"]/text()').extract_first()
        item['close'] = response.xpath('//*[@id="rgt1"]/text()').extract_first()
        item['high'] = response.xpath('//*[@id="rgt3"]/text()').extract_first()
        item['low'] = response.xpath('//*[@id="rgt4"]/text()').extract_first()
        # item['preclose'] = response.xpath('tr[1]/td[2]/span/text()').extract_first()
        item['pctChg'] = self.cutOutTail(response.xpath('//*[@id="rgt5"]/text()').extract_first())  #涨跌幅
        item['volume'] = self.cutOutTail(response.xpath('//*[@id="rgt7"]/text()').extract_first())
        item['amount'] = self.cutOutTail(response.xpath('//*[@id="rgt8"]/text()').extract_first())
        item['turn'] = self.cutOutTail(response.xpath('//*[@id="rgt9"]/text()').extract_first())
        item['peTTM'] = self.cutOutTail(response.xpath('//*[@id="rgt10"]/text()').extract_first())

        item['inner'] = self.cutOutTail(response.xpath('//*[@id="rgt11"]/text()').extract_first())
        item['outer'] = self.cutOutTail(response.xpath('//*[@id="rgt12"]/text()').extract_first())
        item['amplitude'] = self.cutOutTail(response.xpath('//*[@id="rgt13"]/text()').extract_first())
        item['rising_nums'] = response.xpath('//*[@id="rgt14"]/text()').extract_first()

        item['decliner_nums'] = response.xpath('//*[@id="rgt15"]/text()').extract_first()
        item['flat_nums'] = response.xpath('//*[@id="rgt16"]/text()').extract_first()

        # 资金流入情况
        in_out_div = response.xpath('/html/body/div[1]/div[4]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]')
        item['main_inflow'] = self.cutOutTail(in_out_div.xpath('ul[1]/li[2]/span/text()').extract_first())  # 主力流入
        item['main_outflow'] = self.cutOutTail(in_out_div.xpath('ul[2]/li[2]/span/text()').extract_first())  # 主流流出
        item['main_net_inflow'] = self.convert2Y(in_out_div.xpath('ul[3]/li[2]/span/text()').extract_first())  # '主力资金净流入',
        # leading_stock = scrapy.Field()  # '领涨股票',

        yield item

    def cutOutTail(self, funds):
        '''
        截取尾巴
        :param funds:
        :return:
        '''
        if (funds.rfind('亿') != -1):
            funds = funds.replace('亿', '')
        if (funds.rfind('万') != -1):
            funds = funds.replace('万', '')
        if (funds.rfind('%') != -1):
            funds = funds.replace('%', '')
        return funds

    def convert2Y(self, funds):
        if (funds.rfind('亿') != -1):
            return funds.replace('亿', '')
        elif (funds.rfind('万') != -1):
            return float(funds.replace('万', '')) / 10000
