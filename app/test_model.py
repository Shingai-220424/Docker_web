# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Human(Base):
    __tablename__ = 'human'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    height = Column(Float)
    weight = Column(Float)


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    size = Column(Float)
