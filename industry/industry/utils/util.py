from datetime import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class ObjDictTool:
    '''
    实体类和字典转换
    '''

    @staticmethod
    def to_dic(obj):
        '''
        实体转字典
        :param obj: 待转换的实体类
        :return: 字典
        '''
        dic = {}
        for fieldkey in dir(obj):
            fieldvaule = getattr(obj, fieldkey)
            if not fieldkey.startswith("__") and not callable(fieldvaule) and not fieldkey.startswith("_"):
                dic[fieldkey] = fieldvaule
        return dic

    @staticmethod
    def to_obj(obj: object, **data):
        '''
        将字典转实体类
        :param obj: 实体类（输出）
        :param data: 字典（输入）
        :return:
        '''
        obj.__dict__.update(data)


class PinyinTool:
    '''
    拼音工具
    '''

    @staticmethod
    def single_get_first( unicode1):
        '''
        取拼音首字母
        :param unicode1:
        :return:
        '''
        str1 = unicode1.encode('gbk')
        try:
            ord(str1)
            return str1
        except:
            asc = str1[0] * 256 + str1[1] - 65536
            if asc >= -20319 and asc <= -20284:
                return 'a'
            if asc >= -20283 and asc <= -19776:
                return 'b'
            if asc >= -19775 and asc <= -19219:
                return 'c'
            if asc >= -19218 and asc <= -18711:
                return 'd'
            if asc >= -18710 and asc <= -18527:
                return 'e'
            if asc >= -18526 and asc <= -18240:
                return 'f'
            if asc >= -18239 and asc <= -17923:
                return 'g'
            if asc >= -17922 and asc <= -17418:
                return 'h'
            if asc >= -17417 and asc <= -16475:
                return 'j'
            if asc >= -16474 and asc <= -16213:
                return 'k'
            if asc >= -16212 and asc <= -15641:
                return 'l'
            if asc >= -15640 and asc <= -15166:
                return 'm'
            if asc >= -15165 and asc <= -14923:
                return 'n'
            if asc >= -14922 and asc <= -14915:
                return 'o'
            if asc >= -14914 and asc <= -14631:
                return 'p'
            if asc >= -14630 and asc <= -14150:
                return 'q'
            if asc >= -14149 and asc <= -14091:
                return 'r'
            if asc >= -14090 and asc <= -13119:
                return 's'
            if asc >= -13118 and asc <= -12839:
                return 't'
            if asc >= -12838 and asc <= -12557:
                return 'w'
            if asc >= -12556 and asc <= -11848:
                return 'x'
            if asc >= -11847 and asc <= -11056:
                return 'y'
            if asc >= -11055 and asc <= -10247:
                return 'z'
            return ''

    @staticmethod
    def getPinyinAbridge(string):
        '''
        汉字拼音首字母缩写
        :param string:
        :return:
        '''
        if string == None:
            return None
        lst = list(string.replace(" ", ""))
        charLst = []
        for l in lst:
            charLst.append(PinyinTool.single_get_first(l))
        return (''.join(charLst))


class SpiderTool:
    '''
    爬虫工具类
    '''

    @staticmethod
    def isElementPresent(driver, by, value):
        """
        用来判断元素标签是否有下一页，
        """
        try:

            element = driver.find_element(by=by, value=value)
        except NoSuchElementException as e:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True

    @staticmethod
    def pageDown(bro):
        wait = WebDriverWait(bro, 2)
        wait.until(
            lambda driver: driver.find_element_by_link_text('下一页'))  # 内容加载完成后爬取
        next_page = bro.find_element_by_link_text('下一页')
        next_page.click()  # 模拟点击下一页
        time.sleep(5)
