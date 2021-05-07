import scrapy


class IndustryCapitalSpider(scrapy.Spider):
    name = 'industry_capital'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
