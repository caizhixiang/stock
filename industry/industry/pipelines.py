from .items import SectorFundsItem, IndustryStockItem

from orm.dao import IndustrySectorFundsDao, IndustryStockDao


class IndustryPipeline:

    def process_item(self, item, spider):
        if (isinstance(item, SectorFundsItem)):
            # 判断是否是SectorFundsItem
            IndustrySectorFundsDao.save(item)
            # print(item)
        elif (isinstance(item, IndustryStockItem)):
            IndustryStockDao.save(item)
        return item
