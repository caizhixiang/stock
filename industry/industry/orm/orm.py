from sqlalchemy.orm import sessionmaker

from industry.orm.models import engine

DBsession = sessionmaker(bind=engine)
session = DBsession()


def save(Base):
    session.add(Base)
    session.commit()


def updateByParam(Obj, *params, **target):
    '''

    :param Obj: 实体类
    :param params: 查询条件
    :param target: 更新目标值
    :return:
    '''
    session.query(Obj).filter(params).update(target)
    session.commit()


def queryAll(Obj):
    return session.query(Obj).all()


def queryBySql(sql):
    res = session.execute(sql)
    all_res_list = res.fetchall()
    return all_res_list


def queryOneByFilter(Obj, *filters):
    return session.query(Obj).filter(*filters).first()
