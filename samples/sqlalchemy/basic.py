#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
desc: sample

:copyright: (c) 2017 by Xiong Neng.
:license: MIT, see LICENSE for more details.
"""
from samples.sqlalchemy.models import Base, User, Address

if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine('mysql+pymysql://root:winstore@192.168.212.200:3306/test', echo=True)
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)

    session = Session()  # 先使用工程类来创建一个session
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)

    session.add_all([
        User(name='wendy', fullname='Wendy Williams', password='foobar'),
        User(name='mary', fullname='Mary Contrary', password='xxg527'),
        User(name='fred', fullname='Fred Flinstone', password='blah')])
    session.commit()

    # 在session上面调用`query()`方法会创建一个`Query`对象
    for user in session.query(User).order_by(User.id):
        print(user.name, user.fullname)

    # 使用filter_by过滤
    for name in session.query(User.name).filter_by(fullname='Ed Jones'):
        print(name)
    # 使用sqlalchemy的SQL表达式语法过滤，可以使用python语句
    for name in session.query(User.name).filter(User.fullname == 'Ed Jones'):
        print(name)

    # 删除
    session.delete(ed_user)
    print(session.query(User).filter_by(name='ed').count())

    # 通过几个例子来操作一对多的关系映射
    jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
    jack.addresses = [Address(email_address='jack@google.com'),
                      Address(email_address='j25@yahoo.com')]
    session.add(jack)
    session.commit()

    # 查询
    jack = session.query(User).filter_by(name='jack').one()
    # 只有在调用jack.addresses时才会调用查询邮件地址的SQL，这个是典型的懒加载模式
    print(jack.addresses)

    # join查询
    userlist = session.query(User).join(Address).filter(Address.email_address == 'jack@google.com').all()
    print(userlist)

    # 强制加载，不适用懒加载
    from sqlalchemy.orm import joinedload
    jack = session.query(User).options(joinedload(User.addresses)).filter_by(name='jack').one()


