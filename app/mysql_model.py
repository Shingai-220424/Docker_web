# coding: utf-8
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Human(Base):
    __tablename__ = 'human'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    height = Column(Float(asdecimal=True))
    weight = Column(Float(asdecimal=True))


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    size = Column(Float(asdecimal=True))
