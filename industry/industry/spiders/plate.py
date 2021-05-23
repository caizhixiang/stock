import time

import scrapy
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait

from industry.items import SectorFundsItem


class PlateSpider(scrapy.Spider):
    '''
    板块信息
    '''
    name = 'plate'
    start_urls = ['http://data.eastmoney.com/bkzj/hy.html']

    def __init__(self, *args, **kwargs):
        self.bro = Chrome()

    def parse(self, response):
        """模拟浏览器实现翻页，并解析每一个话题列表页的url_list
                       """
        url_set = set()  # 话题url的集合
        self.bro.get(response.url)
        while True:
            wait = WebDriverWait(self.bro, 2)
            wait.until(
                lambda driver: driver.find_element_by_xpath(
                    '//*[@id="dataview"]/div[2]/div[2]/table/tbody/tr'))  # 内容加载完成后爬取
            tr_list = self.bro.find_elements_by_xpath('//*[@id="dataview"]/div[2]/div[2]/table/tbody/tr')
            for tr in tr_list:
                href = tr.find_element_by_xpath('./td[3]/a[1]').get_attribute('href')
                url_set.add(href)
            try:
                wait = WebDriverWait(self.bro, 2)
                wait.until(
                    lambda driver: driver.find_element_by_link_text('下一页'))  # 内容加载完成后爬取
                next_page = self.bro.find_element_by_link_text('下一页')
                next_page.click()  # 模拟点击下一页
                time.sleep(5)
            except:
                print
                "#####Arrive thelast page.#####"
                break

        for url in url_set:
            yield scrapy.Request(url, callback=self.parse_large_order_details)

    def parse_large_order_details(self, response):
        # print(response)
        tr_res = response.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/table/tbody/tr[2]')
        # symbol = tr_res.xpath('./td[3]/span/@class').extract_first()

        item = SectorFundsItem()

        item['industry_name'] = tr_res.xpath('./td[1]/a/text()').extract_first()
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
