'''
Models for user
'''

__author__ = 'caizhixiang'

from .orm import Model, IntegerField, StringField, DateField


class IndustryInfo(Model):
    __table__ = 'industry_info'

    id = IntegerField(primary_key=True)
    name = StringField(ddl='varchar(50)')
    code = StringField(ddl='varchar(50)')
    sector_link = StringField(ddl='varchar(255)')
    quotation_link = StringField(ddl='varchar(255)')
    create_time = DateField()
    update_time = DateField()

