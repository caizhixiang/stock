from twisted.enterprise import adbapi
from twisted.internet import reactor

from industry.settings import MY_MYSQL_SETTINGS
from pymysql import cursors


class orm(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
        self.dicc = []

    def getAge(self, id):
        query = self.dbpool.runQuery("SELECT * FROM industry_info WHERE id = %s", id)
        return query.addCallbacks(self.printResult)

    def printResult(self, l):
        for item in l:
            print(item)
            self.dicc.append(item['id'])


asyn_mysql_settings = MY_MYSQL_SETTINGS
asyn_mysql_settings['cursorclass'] = cursors.DictCursor
dbpool = adbapi.ConnectionPool("pymysql", **asyn_mysql_settings)
o = orm(dbpool)
o.getAge(1)
reactor.callLater(4, reactor.stop)
reactor.run()
print('-------------')
print(o.dicc)
