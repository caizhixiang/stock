import scrapy
from selenium.webdriver import Chrome
from firstBlood.items import FirstbloodItem


class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://data.eastmoney.com/bkzj/hy.html']

    def __init__(self):
        self.bro = Chrome()

    def parse(self, response):
        industry_names = response.xpath(
            '/html/body/div[1]/div[8]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/a/text()').extract()
        industry_links = response.xpath(
            '/html/body/div[1]/div[8]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/a/@href').extract()

        item = FirstbloodItem()
        item['industry_names'] = industry_names
        item['industry_links'] = industry_links

        yield item
