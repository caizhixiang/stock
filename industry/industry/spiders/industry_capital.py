from selenium.webdriver import Chrome

import scrapy

from industry.items import IndustryCapitalItem


class IndustryCapitalSpider(scrapy.Spider):
    name = 'industry_capital'
    start_urls = ['http://data.eastmoney.com/bkzj/hy.html']

    def __init__(self):
        self.bro = Chrome()

    def parse(self, response):
        industry_names = []
        industry_links = []
        tr_list = response.xpath('//*[@id="dataview"]/div[2]/div[2]/table/tbody/tr')
        for tr in tr_list:
            industry_links.append(tr.xpath('./td/a/@href').extract_first())
            industry_names.append(tr.xpath('./td/a/text()').extract_first())

        item = IndustryCapitalItem()
        item['industry_names'] = industry_names
        item['industry_links'] = industry_links

        yield item
