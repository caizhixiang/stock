from sqlalchemy.orm import sessionmaker

from industry.orm.models import engine

DBsession = sessionmaker(bind=engine)
session = DBsession()

def save(Base):
    session.add(Base)
    session.commit()

def queryAll(Obj):
    return session.query(Obj).all()
