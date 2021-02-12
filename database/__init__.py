# encoding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def get_db_session():
    engine = create_engine("sqlite://")
    return scoped_session(sessionmaker(bind=engine))


session = get_db_session()
