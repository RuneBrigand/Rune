import random


from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text, VARBINARY,BLOB,TEXT
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('mysql+pymysql://root:123456@localhost:3306/blog?charset=utf8')
Base = declarative_base()


class Customer(Base):

    __tablename__ = 'customers'

    id = Column(Integer,autoincrement=True, primary_key=True)
    #hash_value = Column(String(64), nullable=False, index=True)
    #pic_value = Column(BLOB(5*1024), nullable=False,index=True)
    #htm_value = Column(TEXT, nullable=False, index=True)

    cus_name=Column(String(64),nullable=False,index=True)
    cus_address=Column(String(64),nullable=False,index=True)
    cus_phone_num=Column(Integer,nullable=False,index=True)


class Prd(Base):

    __tablename__ = 'products'

    id = Column(Integer, autoincrement=True, primary_key=True)

    vendor_id = Column(Integer, nullable=False, index=True)
    prds_name = Column(String(64), nullable=False, index=True)
    price=Column(Integer,nullable=False,index=True)
    state=Column(String(64), nullable=False, index=True)


class Cart(Base):

    __tablename__ = 'carts'

    id = Column(Integer,autoincrement=True, primary_key=True)
    quantity=Column(Integer,nullable=False,index=True)
    prds_id= Column(Integer, nullable=False, index=True)
    cus_id = Column(Integer, nullable=False, index=True)


class Vendor(Base):

    __tablename__ = 'vendors'

    id = Column(Integer,autoincrement=True, primary_key=True)
    vendor_name=Column(String(64),nullable=False,index=True)
    vendor_address=Column(String(64),nullable=False,index=True)
    vendor_phone_num=Column(Integer,nullable=False,index=True)


class Order(Base):

    __tablename__ = 'orders'

    id = Column(Integer,autoincrement=True, primary_key=True)
    cus_id = Column(Integer, nullable=False, index=True)
    cus_name = Column(String(64), nullable=False, index=True)
    cus_address = Column(String(64), nullable=False, index=True)
    cus_phone_num = Column(Integer, nullable=False, index=True)
    vendor_id = Column(Integer, nullable=False, index=True)
    prds_name = Column(String(64), nullable=False, index=True)
    price = Column(Integer, nullable=False, index=True)
    state = Column(String(64), nullable=False, index=True)
    quantity = Column(Integer, nullable=False, index=True)
    total = Column(Integer, nullable=False, index=True)



class Deal(Base):

    __tablename__ = 'deals'

    id = Column(Integer,autoincrement=True, primary_key=True)
    order_id=Column(Integer,nullable=False,index=True)
    condition_id= Column(Integer, nullable=False, index=True)


class Condition(Base):

    __tablename__ = 'conditions'

    id = Column(Integer,autoincrement=True, primary_key=True)
    con=Column(String(64), nullable=False, index=True)
    condition_id= Column(Integer, nullable=False, index=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)