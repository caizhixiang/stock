import datetime
from .items import SectorFundsItem, IndustryStockItem
from .orm.models import IndustrySectorFunds, IndustryInfo, IndustryStock
from .orm.orm import save

class IndustryPipeline:

    def process_item(self, item, spider):
        if (isinstance(item, SectorFundsItem)):
            # 判断是否是SectorFundsItem
            # self.do_funds_insert(item)
            print(item)
        elif (isinstance(item, IndustryStockItem)):
            self.do_industry_stock_insert(item)
        return item

    def db_insert(self, item):
        print("添加数据========================")
        industry_names = item['industry_names']
        sector_links = item['sector_links']
        quotation_links = item['quotation_links']
        for index in range(len(industry_names)):
            sector_link = "http://data.eastmoney.com" + sector_links[index]
            code = sector_link.split("/")[2].split('.')[0]
            name = industry_names[index]
            quotation_link = "http:" + quotation_links[index]
            save(IndustryInfo(name=name,
                              code=code,
                              sector_link=sector_link,
                              quotation_link=quotation_link,
                              create_time=datetime.datetime.now(),
                              update_time=datetime.datetime.now()))

    def do_funds_insert(self, item):
        '''
        保存板块信息
        :param item:
        :return:
        '''
        print("添加数据========================")
        save(IndustrySectorFunds(industry_name=item['industry_name'],
                                 chg=item['chg'],
                                 turnover_rate=item['turnover_rate'],
                                 rising_nums=item['rising_nums'],
                                 decliner_nums=item['decliner_nums'],
                                 leading_stock=item['leading_stock'],
                                 main_net_inflow=item['main_net_inflow'],
                                 super_large_inflow=item['super_large_inflow'],
                                 large_inflow=item['large_inflow'],
                                 middle_inflow=item['middle_inflow'],
                                 small_inflow=item['small_inflow'],
                                 create_time=datetime.datetime.now()))

    def do_industry_stock_insert(self, item):
        '''
        保存板块-股票信息
        :param item:
        :return:
        '''
        print("添加数据========================")
        save(IndustryStock(industry_name=item['industry_name'],
                               stock_code=item['stock_code'],
                               stock_name=item['stock_name'],
                               stock_detail_url=item['stock_detail_url'],
                               create_time=datetime.datetime.now()))


