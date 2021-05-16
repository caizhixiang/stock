# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndustryItem(scrapy.Item):
    '''
    行业数据
    '''
    industry_names = scrapy.Field()
    industry_links = scrapy.Field()


class IndustryCapitalItem(scrapy.Item):
    '''
    行业资金
    '''
    industry_names = scrapy.Field()
    quotation_links = scrapy.Field()
    sector_links = scrapy.Field()


class SectorFundsItem(scrapy.Item):
    '''
    板块信息
    '''
    chg = scrapy.Field() #涨跌幅
    turnover_rate=scrapy.Field() #换手率
    rising_nums=scrapy.Field()#上涨家数
    decliner_nums=scrapy.Field()#下跌家数
    inflows=scrapy.Field()#资金净流入



