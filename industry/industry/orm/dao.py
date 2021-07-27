from datetime import datetime

from industry.utils.util import ObjDictTool, PinyinTool
from industry.orm.models import IndustrySectorFunds, IndustryInfo, IndustryStock
from industry.orm.orm import save,queryAll


class IndustryInfoDao:
    '''
    行业信息
    '''

    def save(self, item):
        print("添加数据========================")
        industry_names = item['industry_names']
        sector_links = item['sector_links']
        # quotation_links = item['quotation_links']
        for index in range(len(industry_names)):
            sector_link = "http://data.eastmoney.com" + sector_links[index]
            code = sector_link.split("/")[2].split('.')[0]
            name = industry_names[index]
            # quotation_link = "http:" + quotation_links[index]
            save(IndustryInfo(name=name,
                              code=code,
                              sector_link=sector_link,
                              # quotation_link=quotation_link,
                              create_time=datetime.now(),
                              update_time=datetime.now()))

    def findAll(self):
        return queryAll(IndustryInfo)



class IndustrySectorFundsDao:
    '''
    行业板块信息
    '''

    def save(self, item):
        '''
        保存板块信息
        :param item:
        :return:
        '''
        print("添加数据========================")
        funds = IndustrySectorFunds()
        ObjDictTool.to_obj(obj=funds, **item)
        funds.__setattr__('create_time', datetime.now())
        save(funds)


class IndustryStockDao:
    '''
    行业股票信息
    '''

    def save(self, item):
        '''
        保存板块-股票信息
        :param item:
        :return:
        '''
        print("添加数据========================")
        stock = IndustryStock()
        ObjDictTool.to_obj(obj=stock, **item)
        stock.__setattr__('create_time', datetime.now())
        stock.__setattr__('abridge', PinyinTool.getPinyinAbridge(stock.__getattribute__('stock_name')))
        save(stock)
