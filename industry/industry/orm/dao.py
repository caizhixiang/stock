from datetime import datetime

from industry.orm.models import IndustrySectorFunds, IndustryInfo, IndustryStock, StockMarket
from industry.orm.orm import save, queryAll
from industry.utils.util import ObjDictTool, PinyinTool


class IndustryInfoDao:
    '''
    行业信息
    '''

    def save(self, item):
        print("添加数据========================")
        industry_names = item['industry_names']
        industry_links = item['industry_links']
        # sector_links = item['sector_links']
        # quotation_links = item['quotation_links']
        for name, link in zip(industry_names, industry_links):
            code = link[link.rfind(".") + 1:]
            # quotation_link = "http:" + quotation_links[index]
            save(IndustryInfo(name=name,
                              code=code,
                              # sector_link=sector_link,
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
        try:
            stock.__setattr__('abridge', PinyinTool.getPinyinAbridge(stock.__getattribute__('stock_name')))
        except:
            print(stock.__getattribute__('stock_name'))
            print(PinyinTool.getPinyinAbridge(stock.__getattribute__('stock_name')))
        save(stock)


class StockMarketDao:
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
        # 先根据日期和code查询有没有记录，没有则新增，有则更新
        # session=DBsession()
        # data = session.query(StockMarket).filter_by(market_code=item['market_code'],
        #                                             create_time=item['creat_time']).first()
        # if data:
        #     {setattr(data, k, v) for k, v in item.items()}
        #     print(data)
        # else:
        #     stockMarket = StockMarket()
        #     ObjDictTool.to_obj(obj=stockMarket, **item)
        #     create_time = item["creat_time"]
        #     time_split = create_time.split("-")
        #
        #     date_time = datetime(int(time_split[0]), month=int(time_split[1]), day=int(time_split[2]), hour=15)
        #     stockMarket.__setattr__('create_time', date_time)
        #     save(stockMarket)
