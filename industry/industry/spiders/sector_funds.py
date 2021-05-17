from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium.webdriver import Chrome

from industry.items import SectorFundsItem


class SectorFundsSpider(CrawlSpider):
    name = 'sector_funds'
    start_urls = ['http://data.eastmoney.com/bkzj/hy.html']

    rules = (
        Rule(LinkExtractor(allow=r'bkzj/BK\d+\.html'), callback='parse_large_order_details', follow=False),
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

        item['industry_name']=tr_res.xpath('./td[1]/a/text()').extract_first()
        item['chg'] = tr_res.xpath('./td[3]/span/text()').extract_first().replace('%', '')

        item['turnover_rate'] = tr_res.xpath('./td[4]/text()').extract_first().replace('%', '')
        item['rising_nums'] = tr_res.xpath('./td[5]/span/text()').extract_first()
        item['decliner_nums'] = tr_res.xpath('./td[6]/span/text()').extract_first()

        item['leading_stock'] = tr_res.xpath('./td[7]/a/text()').extract_first()

        # 资金流入情况
        funds_tr_res = response.xpath('/html/body/div[1]/div[8]/div[2]/div[5]/div[1]/table/tbody')

        item['main_net_inflow'] = self.convert2W(funds_tr_res.xpath('./tr[1]/td[3]/span/text()').extract_first())

        item['super_large_inflow'] = self.convert2W(funds_tr_res.xpath('./tr[2]/td[3]/span/text()').extract_first())

        item['large_inflow'] = self.convert2W(funds_tr_res.xpath('./tr[3]/td[3]/span/text()').extract_first())

        item['middle_inflow'] = self.convert2W(funds_tr_res.xpath('./tr[4]/td[3]/span/text()').extract_first())

        item['small_inflow'] = self.convert2W(funds_tr_res.xpath('./tr[5]/td[3]/span/text()').extract_first())


        return item

    def convert2W(self, funds):
        if (funds.rfind('万') != -1):
            return funds.replace('万', '')
        elif (funds.rfind('亿') != -1):
            return float(funds.replace('亿', '')) * 4
