from .items import SectorFundsItem, StockInfoItem, IndustryItem, StockMarketItem

from orm.dao import IndustrySectorFundsDao, IndustryStockDao, IndustryInfoDao, StockMarketDao


class IndustryPipeline:

    def process_item(self, item, spider):
        if (isinstance(item, SectorFundsItem)):
            # 判断是否是SectorFundsItem
            IndustrySectorFundsDao().save(item)
            # print(item)
        elif (isinstance(item, StockInfoItem)):
            IndustryStockDao.save(item)
        elif (isinstance(item,IndustryItem)):
            IndustryInfoDao().save(item)
        elif (isinstance(item,StockMarketItem)):
            StockMarketDao().save(item)
        return item
