from scrapy.cmdline import execute
import os
import sys

def str_of_num( num):
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

if __name__ == '__main__':
    # sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # execute(['scrapy', 'crawl', 'first'])
    print(str_of_num(1000000000))


