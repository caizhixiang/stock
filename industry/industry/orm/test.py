from industry.orm.models import IndustryInfo
from industry.orm import  orm
import asyncio


orm.create_pool()

u = IndustryInfo()
find = u.find(IndustryInfo, 1)
print(find)