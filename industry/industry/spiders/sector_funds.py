from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium.webdriver import Chrome


class SectorFundsSpider(CrawlSpider):
    name = 'sector_funds'
    start_urls = ['http://data.eastmoney.com/bkzj/hy.html']
#https://blog.csdn.net/elecjack/article/details/51532482?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-3.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-3.control
    # https://www.jianshu.com/p/e821389ad437?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
    rules = (
        Rule(LinkExtractor(allow='http://data.eastmoney.com/bkzj/hy.html'), callback='parse_item', follow=True),
        Rule(
            LinkExtractor(
                allow=r'bkzj/BK\d+\.html',
                restrict_xpaths=('//*[@id="dataview"]/div[2]/div[2]/table/tbody'),
                # 限制提取链接的范围, 支持xpath
            ),
            callback='parse_large_order_details', follow=False),
    )

    def __init__(self, *args, **kwargs):
        super(SectorFundsSpider, self).__init__(*args, **kwargs)  # 这里是关键
        self.bro = Chrome()

    def parse_item(self, response):
        print(response)
        xpath = self.bro.find_element_by_xpath('//*[@id="dataview"]/div[3]/div[1]/a[3]')
        if xpath!=None:
            xpath.click()
        # yield item

    def parse_large_order_details(self, response):
        print(response)
        # tr_res = response.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/table/tbody/tr[2]')
        # symbol = tr_res.xpath('./td[3]/span/@class').extract_first()
        #
        # item = SectorFundsItem()
        #
        # item['industry_name'] = tr_res.xpath('./td[1]/a/text()').extract_first()
        # item['chg'] = tr_res.xpath('./td[3]/span/text()').extract_first().replace('%', '')
        #
        # item['turnover_rate'] = tr_res.xpath('./td[4]/text()').extract_first().replace('%', '')
        # item['rising_nums'] = tr_res.xpath('./td[5]/span/text()').extract_first()
        # item['decliner_nums'] = tr_res.xpath('./td[6]/span/text()').extract_first()
        #
        # item['leading_stock'] = tr_res.xpath('./td[7]/a/text()').extract_first()
        #
        # # 资金流入情况
        # funds_tr_res = response.xpath('/html/body/div[1]/div[8]/div[2]/div[5]/div[1]/table/tbody')
        #
        # item['main_net_inflow'] = self.convert2W(funds_tr_res.xpath('./tr[1]/td[3]/span/text()').extract_first())
        #
        # item['super_large_inflow'] = self.convert2W(funds_tr_res.xpath('./tr[2]/td[3]/span/text()').extract_first())
        #
        # item['large_inflow'] = self.convert2W(funds_tr_res.xpath('./tr[3]/td[3]/span/text()').extract_first())
        #
        # item['middle_inflow'] = self.convert2W(funds_tr_res.xpath('./tr[4]/td[3]/span/text()').extract_first())
        #
        # item['small_inflow'] = self.convert2W(funds_tr_res.xpath('./tr[5]/td[3]/span/text()').extract_first())
        #
        # return item

    def convert2W(self, funds):
        if (funds.rfind('万') != -1):
            return funds.replace('万', '')
        elif (funds.rfind('亿') != -1):
            return float(funds.replace('亿', '')) * 4
