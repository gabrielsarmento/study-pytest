# encoding: utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer


Base = declarative_base()


class PointModel(Base):
    __tablename__ = 'points'

    id = Column(Integer, primary_key=True)
    x = Column(Integer, default=0)
    y = Column(Integer, default=0)
