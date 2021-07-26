from selenium.webdriver import Chrome

import scrapy

from industry.items import IndustryCapitalItem


class IndustryCapitalSpider(scrapy.Spider):
    '''
    行业资金流入情况
    '''
    name = 'industry_capital'
    start_urls = ['http://data.eastmoney.com/bkzj/hy.html']

    def __init__(self):
        self.bro = Chrome()

    def parse(self, response):
        industry_names = []
        sector_links = []
        quotation_links = []
        tr_list = response.xpath('//*[@id="dataview"]/div[2]/div[2]/table/tbody/tr')
        for tr in tr_list:
            quotation_links.append(tr.xpath('./td/a/@href').extract_first())
            sector_links.append(tr.xpath('./td/a/@href')[1].extract())
            industry_names.append(tr.xpath('./td/a/text()').extract_first())

        item = IndustryCapitalItem()
        item['industry_names'] = industry_names
        item['sector_links'] = sector_links
        item['quotation_links'] = quotation_links

        yield item
