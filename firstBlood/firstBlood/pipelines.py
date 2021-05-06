# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

from dto import industry_info
from .settings import MY_MYSQL_SETTINGS
from pymysql import cursors
# twisted 网络框架
# API 接口
from twisted.enterprise import adbapi
import datetime


class FirstbloodPipeline:
    # 从配置文件中读取配置
    @classmethod
    def from_settings(cls, settings):
        asyn_mysql_settings = MY_MYSQL_SETTINGS
        asyn_mysql_settings['cursorclass'] = cursors.DictCursor
        dbpool = adbapi.ConnectionPool("pymysql", **asyn_mysql_settings)
        return cls(dbpool)

    def __init__(self, dbpool):
        self.dbpool = dbpool

        query = self.dbpool.runInteraction(self.db_create)
        query.addErrback(self.db_create_err)

    def db_create(self, cursor):
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS `industry_info` (
                      `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
                      `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '行业名称',
                      `code` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '行业编码',
                      `link` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '行业跳转链接',
                      `create_time` datetime NULL DEFAULT NULL COMMENT '创建时间',
                      `update_time` datetime NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
                      PRIMARY KEY (`id`) USING BTREE
                    ) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '行业信息' ROW_FORMAT = Dynamic;
                    """)

    def db_create_err(self, failure):
        print('---------------------------', failure)

    # def open_spider(self, spider):
    #     self.dbpool = dbpool
    #
    #     query = self.dbpool.runInteraction(self.db_create)
    #     query.addErrback(self.db_create_err)

    # def close_spider(self, spider):
    #     self.dbpool.close()

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.db_insert, item)
        query.addErrback(self.handle_error, item)
        return item

    def handle_error(self, failure, item):
        print('============================', failure, item)

    def db_insert(self, cursor, item):
        print("添加数据========================")
        industry_names = item['industry_names']
        industry_links = item['industry_links']
        for index in range(len(industry_names)):
            link = industry_links[index]
            code = link.split("/")[2].split('.')[0]
            name = industry_names[index]
            cursor.execute("""
                           INSERT INTO industry_info (  `name`, `code`, `link`, `create_time` ) VALUES ( %s,%s,%s,%s)
                           """, (name, code, link, datetime.datetime.now()))
