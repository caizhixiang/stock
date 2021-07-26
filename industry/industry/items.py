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
    industry_name = scrapy.Field()  # '板块名称'
    industry_code = scrapy.Field()  # '板块code'
    open = scrapy.Field()  # '开盘价'
    close = scrapy.Field()  # '收盘价'
    high = scrapy.Field()  # '最高价'
    low = scrapy.Field()  # '最低价'
    preclose = scrapy.Field()  # '前收盘价',
    volume = scrapy.Field()  # '成交量（累计 单位：股）',
    amount = scrapy.Field()  # '成交额',
    inner = scrapy.Field()  # '内盘',
    outer = scrapy.Field()  # '外盘',
    peTTM = scrapy.Field()  # '流通市值	',
    pctChg = scrapy.Field()  # '涨跌幅',
    amplitude = scrapy.Field()  # '振幅',
    turn = scrapy.Field()  # '换手率',
    rising_nums = scrapy.Field()  # '上涨家数',
    decliner_nums = scrapy.Field()  # '下跌家数',
    flat_nums = scrapy.Field()  # '平家数',
    leading_stock = scrapy.Field()  # '领涨股票',
    main_inflow=scrapy.Field()  #主力流入
    main_outflow=scrapy.Field() #主流流出
    main_net_inflow = scrapy.Field()  # '主力资金净流入',
    super_large_inflow = scrapy.Field()  # '超级大单资金净流入',
    large_inflow = scrapy.Field()  # '大单净流入',
    middle_inflow = scrapy.Field()  # '中单净流入',
    small_inflow = scrapy.Field()  # '小单净流入',


class IndustryStockItem(scrapy.Item):
    '''
    板块——股票信息
    '''

    stock_code = scrapy.Field()
    stock_name = scrapy.Field()
    stock_detail_url = scrapy.Field()
    industry_name = scrapy.Field()
