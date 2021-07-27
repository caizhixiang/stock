import time

import scrapy
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait

from industry.items import IndustryItem


class IndustryInfoSpider(scrapy.Spider):
    '''
    行业信息数据
    '''
    name = 'industry_info'
    # allowed_domains = ['example.com']
    start_urls = ['http://data.eastmoney.com/bkzj/hy.html']

    def __init__(self):
        self.bro = Chrome()

    def parse(self, response):
        # itemSet = set()
        # industry_names = response.xpath(
        #     '/html/body/div[1]/div[8]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/a/text()').extract()
        # industry_links = response.xpath(
        #     '/html/body/div[1]/div[8]/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/a/@href').extract()
        #
        item = IndustryItem()
        item['industry_names'] = set()
        item['industry_links'] = set()
        # itemSet.add(item)
        self.pageDown(response, item)
        # for itemm in itemSet:
        yield item

    def pageDown(self, response, item):
        self.bro.get(response.url)
        while True:
            wait = WebDriverWait(self.bro, 2)
            wait.until(
                lambda driver: driver.find_element_by_xpath(
                    '//*[@id="dataview"]/div[2]/div[2]/table/tbody/tr'))  # 内容加载完成后爬取
            tr_list = self.bro.find_elements_by_xpath('//*[@id="dataview"]/div[2]/div[2]/table/tbody/tr')
            for tr in tr_list:
                href = tr.find_element_by_xpath('./td[2]/a[1]').get_attribute('href')
                name = tr.find_element_by_xpath('./td[2]/a[1]').text
                item['industry_names'].add(name)
                item['industry_links'].add(href)

            try:
                self.pageNext()
            except Exception:
                print("#####Arrive thelast page.#####")
                break

    def pageNext(self):
        wait = WebDriverWait(self.bro, 2)
        wait.until(
            lambda driver: driver.find_element_by_link_text('下一页'))  # 内容加载完成后爬取
        next_page = self.bro.find_element_by_link_text('下一页')
        next_page.click()  # 模拟点击下一页
        time.sleep(5)