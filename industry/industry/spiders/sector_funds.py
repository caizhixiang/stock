from selenium.webdriver import Chrome

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from industry.items import SectorFundsItem


class SectorFundsSpider(CrawlSpider):
    name = 'sector_funds'
    start_urls = ['http://data.eastmoney.com/bkzj/hy.html']

    rules = (
        Rule(LinkExtractor(allow=r'bkzj/BK\d+\.html'), callback='parse_large_order_details', follow=True),
    )

    def __init__(self, *args, **kwargs):
        super(SectorFundsSpider, self).__init__(*args, **kwargs)  # 这里是关键
        self.bro = Chrome()

    def parse_item(self, response):
        item = SectorFundsItem()
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    def parse_large_order_details(self, response):
        tr_res = response.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/table/tbody/tr[2]')
        symbol = tr_res.xpath('./td[3]/span/@class').extract_first()

        item = SectorFundsItem()
        item['chg'] = tr_res.xpath('./td[3]/span/text()').extract_first()
        item['turnover_rate'] = tr_res.xpath('./td[4]/text()').extract_first()
        item['rising_nums'] = tr_res.xpath('./td[5]/span/text()').extract_first()
        item['decliner_nums'] = tr_res.xpath('./td[6]/span/text()').extract_first()
        # item['inflows']
        print(response)
