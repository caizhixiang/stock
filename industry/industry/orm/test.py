from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from industry.orm.models import IndustryInfo

engine = create_engine('mysql+pymysql://root:123456@localhost/stock')

DBsession = sessionmaker(bind=engine)
dbsession = scoped_session(DBsession)

meta_data = MetaData(bind=engine)

Base = declarative_base()

if __name__ == '__main__':
    info__all = dbsession.query(IndustryInfo).filter(IndustryInfo.id == 1).all()
    print(info__all)
