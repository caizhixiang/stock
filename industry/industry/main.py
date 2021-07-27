from scrapy.cmdline import execute
import os
import sys

if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # 行业信息  1/
    # execute(['scrapy', 'crawl', 'industry_info'])

    # 行业资金（不分页）
    # execute(['scrapy', 'crawl', 'industry_capital'])

    # 行业资金（分页）
    # execute(['scrapy', 'crawl', 'sector_funds'])
    # 2、行情
    execute(['scrapy', 'crawl', 'sector_quotation'])
    # execute(['scrapy', 'crawl', 'plate'])
