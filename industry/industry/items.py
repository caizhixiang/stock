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
    chg = scrapy.Field()  # 涨跌幅
    turnover_rate = scrapy.Field()  # 换手率
    rising_nums = scrapy.Field()  # 上涨家数
    decliner_nums = scrapy.Field()  # 下跌家数
    main_net_inflow = scrapy.Field()  # 主力资金净流入
    super_large_inflow = scrapy.Field()  # 超大单净流入
    large_inflow = scrapy.Field()  # 大单净流入
    middle_inflow = scrapy.Field()  # 中单净流入
    small_inflow = scrapy.Field()  # 小单净流入
    leading_stock = scrapy.Field()  # 领涨股
    industry_name = scrapy.Field()  # 板块名称
