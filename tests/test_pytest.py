# encoding: utf-8

import pytest
from database import session
from models.models import Base, PointModel
from models.factories import PointFactory


@pytest.fixture
def db_session():
    db_session = session
    Base.metadata.create_all(bind=db_session.bind)
    yield db_session
    Base.metadata.drop_all(bind=db_session.bind)
    # db_session.close()


@pytest.fixture
def point_db(db_session):
    model = PointFactory()
    db_session.add(model)
    db_session.commit()
    yield model
    db_session.delete(model)
    db_session.commit()


def test_a(point_db):
    assert point_db.x == 1


def test_b(db_session):
    result = db_session.query(PointModel).all()
    assert not result

    model = PointFactory()
    db_session.add(model)

    result = db_session.query(PointModel).all()
    assert result


def test_c(db_session):
    result = db_session.query(PointModel).all()
    assert not result
