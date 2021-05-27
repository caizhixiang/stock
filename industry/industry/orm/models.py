from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:123456@localhost/stock')

meta_data = MetaData(bind=engine)

Base = declarative_base()


class IndustryInfo(Base):
    __table__ = Table('industry_info', meta_data, autoload=True)


class IndustrySectorFunds(Base):
    __table__ = Table('industry_sector_funds', meta_data, autoload=True)


class IndustryStock(Base):
    __table__ = Table('industry_stock', meta_data, autoload=True)
