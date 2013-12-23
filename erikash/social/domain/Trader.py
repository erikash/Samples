from sqlalchemy import Column, Integer
from erikash.social.SessionFactory import Base
from erikash.social.domain.OpenPosition import OpenPosition

__author__ = 'erik'


class Trader(Base):
    __tablename__ = 'traders'
    id = Column(Integer, primary_key=True)

    def __init__(self, open_positions=[]):
        self.open_positions = open_positions

    def open_position(self, instrument, amount):
        position = OpenPosition(instrument, amount)
        self.open_positions.append(position)


