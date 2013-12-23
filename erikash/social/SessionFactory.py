__author__ = 'erik'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class SessionFactory(object):
    def __init__(self):
        self._engine = create_engine('postgresql://localhost:5432/test')
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)

        self.session_creator = sessionmaker(bind=self._engine)

    def create_session(self):
        return self.session_creator()


