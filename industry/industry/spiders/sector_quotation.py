import scrapy
from scrapy import Request
from selenium.webdriver import Chrome

from industry.items import SectorFundsItem
from industry.orm.dao import IndustryInfoDao


class SectorQuotationSpider(scrapy.Spider):
    '''
    行业行情数据（涨幅，资金情况）
    '''
    name = 'sector_quotation'

    def start_requests(self):
        '''
        代替start_urls,从数据库读取板块编码，拼接读取板块的行情数据
        :return: 示例：http://quote.eastmoney.com/bk/90.BK0421.html
        '''
        url = 'http://quote.eastmoney.com/bk/90.%s.html'
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
        # 涨幅情况
        increase_tbody = response.xpath('/html/body/div[1]/div[4]/div[3]/div[1]/div[3]/table/tbody')

        item = SectorFundsItem()
        item['industry_name'] = response.xpath('/html/body/div[1]/div[2]/div/span[1]/text()').extract_first()
        item['industry_code'] = response.xpath('/html/body/div[1]/div[2]/div/span[2]/text()').extract_first()
        item['open'] = increase_tbody.xpath('tr[1]/td[1]/span/text()').extract_first()
        item['close'] = increase_tbody.xpath('tr[1]/td[2]/span/text()').extract_first()
        item['high'] = increase_tbody.xpath('tr[2]/td[1]/span/text()').extract_first()
        item['low'] = increase_tbody.xpath('tr[2]/td[2]/span/text()').extract_first()
        # item['preclose'] = increase_tbody.xpath('tr[1]/td[2]/span/text()').extract_first()
        item['pctChg'] = self.cutOutTail(increase_tbody.xpath('tr[3]/td[1]/span/text()').extract_first())
        item['volume'] = self.cutOutTail(increase_tbody.xpath('tr[4]/td[1]/span/text()').extract_first())
        item['amount'] = self.cutOutTail(increase_tbody.xpath('tr[4]/td[2]/span/text()').extract_first())
        item['turn'] = self.cutOutTail(increase_tbody.xpath('tr[5]/td[1]/span/text()').extract_first())
        item['peTTM'] = self.cutOutTail(increase_tbody.xpath('tr[5]/td[2]/span/text()').extract_first())

        item['inner'] = self.cutOutTail(increase_tbody.xpath('tr[6]/td[1]/span/text()').extract_first())
        item['outer'] = self.cutOutTail(increase_tbody.xpath('tr[6]/td[2]/span/text()').extract_first())
        item['amplitude'] = self.cutOutTail(increase_tbody.xpath('tr[7]/td[1]/span/text()').extract_first())
        item['rising_nums'] = increase_tbody.xpath('tr[7]/td[2]/span/text()').extract_first()

        item['decliner_nums'] = increase_tbody.xpath('tr[8]/td[1]/span/text()').extract_first()
        item['flat_nums'] = increase_tbody.xpath('tr[8]/td[2]/span/text()').extract_first()

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