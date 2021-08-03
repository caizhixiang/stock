import json

import scrapy
from selenium.webdriver import Chrome

from industry.items import StockMarketItem


class StockMarketHistorySpider(scrapy.Spider):
    '''
       大盘历史行情（沪市，深市，创业板）

       http://quote.eastmoney.com/concept/sh603259.html#(个股行情)

       上证日k全屏
       http://quote.eastmoney.com/zs000001.html#fullScreenChart
       2021.02.01以来的大盘涨跌幅
       http://61.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery331020473188151630217_1627747598798&secid=1.000001&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&end=20500101&lmt=120&_=1627747598805
       历史所有日期的大盘涨跌幅
       http://9.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery331020473188151630217_1627747598798&secid=1.000001&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&beg=0&end=20500101&smplmt=987&lmt=1000000&_=1627747598804
       '''
    name = 'stock_market_history'
    start_urls = [

        'http://61.push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery331020473188151630217_1627747598798&secid=1.000001&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101&fqt=1&end=20500101&lmt=120&_=1627747598805'

    ]

    def __init__(self, *args, **kwargs):
        self.bro = Chrome()

    def parse(self, response):

        '''
        '2021-08-02,                    成交量     成交额          振幅  涨跌幅  涨跌额  换手率
3385.69,3464.29,3464.29,3367.64,432927872,657885782016.00, 2.84,  1.97,   66.93,  1.11'
1         2         3       4      5         6              7       8       9      10
        :param response:
        :return:
        '''
        print(response)
        text = response.text
        startIndex = text.find('(')
        endIndex = text.rfind(')')
        json_str = text[startIndex + 1:endIndex]
        dic_res = json.loads(json_str)
        data_ = dic_res['data']

        klines_list = data_['klines']

        for kline in klines_list:
            # 大盘指数
            item = StockMarketItem()

            item['market_name'] = data_['name']
            item['market_code'] = data_['code']
            kline_split = kline.split(',')
            item['creat_time'] = kline_split[0]
            item['open'] = kline_split[1]
            item['close'] = kline_split[2]
            item['high'] = kline_split[3]
            item['low'] = kline_split[4]
            # item['preclose'] = response.xpath('tr[1]/td[2]/span/text()').extract_first()
            item['pctChg'] = kline_split[8]  # 涨跌幅
            item['volume'] = self.str_of_num(float(kline_split[5]))  # 成交量 ->亿手
            item['amount'] = self.str_of_num(float(kline_split[6]))  # 成交额  ->亿元
            item['amplitude'] = kline_split[7]  # 振幅
            item['turn'] = kline_split[10]  #
            # item['peTTM'] = self.cutOutTail(response.xpath('//*[@id="rgt10"]/text()').extract_first())  # 流动市值  万亿
            #
            # item['inner'] = self.cutOutTail(response.xpath('//*[@id="rgt11"]/text()').extract_first())  # 万手
            # item['outer'] = self.cutOutTail(response.xpath('//*[@id="rgt12"]/text()').extract_first())  # 万手
            # item['rising_nums'] = self.cutOutTail(response.xpath('//*[@id="rgt14"]/text()').extract_first())  # 家
            #
            # item['decliner_nums'] = self.cutOutTail(response.xpath('//*[@id="rgt15"]/text()').extract_first())  # 家
            # item['flat_nums'] = self.cutOutTail(response.xpath('//*[@id="rgt16"]/text()').extract_first())  # 家

            # 资金流入情况
            # item['main_inflow'] = self.convert2Y(response.xpath('//*[@id="hz_a"]/text()').extract_first())  # 主力流入 亿元
            # item['main_outflow'] = self.convert2Y(response.xpath('//*[@id="hz_b"]/text()').extract_first())  # 主流流出  亿元
            # item['main_net_inflow'] = self.convert2Y(
            #     response.xpath('//*[@id="hz_c"]/text()').extract_first())  # '主力资金净流入'   亿元
            # leading_stock = scrapy.Field()  # '领涨股票',
            yield item

    def convert2Y(self, funds):
        if (funds.rfind('亿元') != -1):
            return funds.replace('亿元', '')
        if (funds.rfind('亿') != -1):
            return funds.replace('亿', '')
        elif (funds.rfind('万') != -1):
            return float(funds.replace('万', '')) / 10000

    def str_of_num(self, num):
        '''
        递归实现，精确为最大单位值 + 小数点后三位
        '''

        def strofsize(num, level):
            if level >= 2:
                return num, level
            elif num >= 10000:
                num /= 10000
                level += 1
                return strofsize(num, level)
            else:
                return num, level

        units = ['', '万', '亿']
        num, level = strofsize(num, 0)
        if level > len(units):
            level -= 1
        return '{}{}'.format(round(num, 3), units[level])
