from .items import SectorFundsItem, IndustryStockItem, IndustryItem

from orm.dao import IndustrySectorFundsDao, IndustryStockDao, IndustryInfoDao


class IndustryPipeline:

    def process_item(self, item, spider):
        if (isinstance(item, SectorFundsItem)):
            # 判断是否是SectorFundsItem
            IndustrySectorFundsDao().save(item)
            # print(item)
        elif (isinstance(item, IndustryStockItem)):
            IndustryStockDao.save(item)
        elif (isinstance(item,IndustryItem)):
            IndustryInfoDao().save(item)
        return item
