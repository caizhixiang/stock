import scrapy
from scrapy import Request
from selenium.webdriver import Chrome

from industry.items import StockInfoItem
from industry.orm.dao import IndustryInfoDao


class StockInfoSpider(scrapy.Spider):
    '''
    股票信息
    '''
    name = 'stock_info'

    def start_requests(self):
        '''
        代替start_urls,从数据库读取板块编码，拼接读取股票信息
        :return: 示例：http://data.eastmoney.com/bkzj/BK0537.html
        '''
        url = 'http://data.eastmoney.com/bkzj/%s.html'
        dao = IndustryInfoDao()
        find_all = dao.findAll()
        if find_all:
            for industryInfo in find_all:
                if industryInfo:
                    code = industryInfo.__getattribute__("code")
                    if code:
                        start_url = url % code
                        yield Request(start_url, callback=self.parse_item)

    def __init__(self, *args, **kwargs):
        self.bro = Chrome()

    def parse_item(self, response):

        # 股票tr
        tr_stocks = response.xpath('//*[@id="dataview"]/div[2]/div[2]/table/tbody/tr')
        for tr_stock in tr_stocks:
            stock_code = tr_stock.xpath('./td[2]/a/text()').extract_first()
            stock_name = tr_stock.xpath('./td[3]/a/text()').extract_first()
            stock_detail_url = tr_stock.xpath('./td[3]/a/@href').extract_first()
            stock_item = StockInfoItem()
            stock_item['stock_code'] = stock_code
            stock_item['stock_name'] = stock_name
            stock_item['stock_detail_url'] = stock_detail_url
            # stock_item['industry_name'] = item['industry_name']
            yield stock_item

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
