# encoding: utf-8

from factory.alchemy import SQLAlchemyModelFactory

from models import PointModel
from database import session


class PointFactory(SQLAlchemyModelFactory):
    class Meta:
        model = PointModel
        sqlalchemy_session = session

    x = 1
    y = 2
