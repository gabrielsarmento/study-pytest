# encoding: utf-8

from unittest import TestCase

from database import session
from models.models import Base,  PointModel
from models.factories import PointFactory


class TestDbSession(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDbSession, self).__init__(*args, **kwargs)

        self.db_session = session

    def setUp(self):
        Base.metadata.create_all(bind=self.db_session.bind)

        self.db_point = PointFactory()

    def tearDown(self):
        Base.metadata.drop_all(bind=self.db_session.bind)

        self.db_session.close()

    def test_a(self):
        self.assertEquals(self.db_point.x, 1)

    def test_b(self):
        result = self.db_session.query(PointModel).all()
        self.assertEquals(len(result), 1)

        self.db_session.add(PointFactory())

        result = self.db_session.query(PointModel).all()
        self.assertEquals(len(result), 2)

    def test_c(self):
        result = self.db_session.query(PointModel).all()
        self.assertEquals(len(result), 1)
