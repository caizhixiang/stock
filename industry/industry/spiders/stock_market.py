import scrapy
from selenium.webdriver import Chrome

from industry.items import StockMarketItem


class StockMarketSpider(scrapy.Spider):
    '''
    大盘行情（沪市，深市，创业板）

    http://quote.eastmoney.com/concept/sh603259.html#(个股行情)

    上证日k全屏
    http://quote.eastmoney.com/zs000001.html#fullScreenChart
    2021.02.01以来的大盘涨跌幅
    http://61.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery331020473188151630217_1627747598798&secid=1.000001&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&end=20500101&lmt=120&_=1627747598805
    历史所有日期的大盘涨跌幅
    http://9.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery331020473188151630217_1627747598798&secid=1.000001&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&beg=0&end=20500101&smplmt=987&lmt=1000000&_=1627747598804
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
        item['pctChg'] = self.cutOutTail(response.xpath('//*[@id="rgt5"]/text()').extract_first())  # 涨跌幅
        item['volume'] = self.cutOutTail(response.xpath('//*[@id="rgt7"]/text()').extract_first())  # 亿手
        item['amount'] = self.cutOutTail(response.xpath('//*[@id="rgt8"]/text()').extract_first())  # 亿
        item['turn'] = self.cutOutTail(response.xpath('//*[@id="rgt9"]/text()').extract_first())  # %
        item['peTTM'] = self.cutOutTail(response.xpath('//*[@id="rgt10"]/text()').extract_first())  # 流动市值  万亿

        item['inner'] = self.cutOutTail(response.xpath('//*[@id="rgt11"]/text()').extract_first())  # 万手
        item['outer'] = self.cutOutTail(response.xpath('//*[@id="rgt12"]/text()').extract_first())  # 万手
        item['amplitude'] = self.cutOutTail(response.xpath('//*[@id="rgt13"]/text()').extract_first())  #振幅
        item['rising_nums'] = self.cutOutTail(response.xpath('//*[@id="rgt14"]/text()').extract_first())   #家

        item['decliner_nums'] = self.cutOutTail(response.xpath('//*[@id="rgt15"]/text()').extract_first())   #家
        item['flat_nums'] = self.cutOutTail(response.xpath('//*[@id="rgt16"]/text()').extract_first())   #家

        # 资金流入情况
        item['main_inflow'] = self.convert2Y(response.xpath('//*[@id="hz_a"]/text()').extract_first())  # 主力流入 亿元
        item['main_outflow'] = self.convert2Y(response.xpath('//*[@id="hz_b"]/text()').extract_first())  # 主流流出  亿元
        item['main_net_inflow'] = self.convert2Y(
            response.xpath('//*[@id="hz_c"]/text()').extract_first())  # '主力资金净流入'   亿元
        # leading_stock = scrapy.Field()  # '领涨股票',

        yield item

    def cutOutTail(self, funds):
        '''
        截取尾巴
        :param funds:
        :return:
        '''
        if (funds.rfind('亿手') != -1):
            funds = funds.replace('亿手', '')
        if (funds.rfind('万手') != -1):
            funds = funds.replace('万手', '')
        if (funds.rfind('亿') != -1):
            funds = funds.replace('亿', '')
        if (funds.rfind('万') != -1):
            funds = funds.replace('万', '')
        if (funds.rfind('%') != -1):
            funds = funds.replace('%', '')
        if (funds.rfind('家') != -1):
            funds = funds.replace('家', '')
        return funds

    def convert2Y(self, funds):
        if (funds.rfind('亿元') != -1):
            return funds.replace('亿元', '')
        if (funds.rfind('亿') != -1):
            return funds.replace('亿', '')
        elif (funds.rfind('万') != -1):
            return float(funds.replace('万', '')) / 10000
