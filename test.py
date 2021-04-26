from config import toDict
import config_default

import  orm.orm
import asyncio
from orm.models import User


def testDB():
    configs = toDict(config_default.configs)
    host = configs.get("db").get("host")
    print(host)


async def testInsert(loop):
    await orm.orm.create_pool(loop=loop)

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(testInsert(loop))
