from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from industry.orm.models import IndustryInfo, engine

DBsession = sessionmaker(bind=engine)
session = DBsession()

def save(Base):
    session.add(Base)
    session.commit()

#
# def update(Base):
#     session.query(Base).filter()

if __name__ == '__main__':
    # info__all = session.query(IndustryInfo).filter(IndustryInfo.id == 1).first()
    # print(info__all)
    industry_info = IndustryInfo(name='shishi', code='dd')

    save(industry_info)
