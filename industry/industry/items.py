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
