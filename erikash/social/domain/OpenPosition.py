from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from erikash.social.SessionFactory import Base

__author__ = 'erik'


class OpenPosition(Base):
    __tablename__ = 'open_positions'
    id = Column(Integer, primary_key=True)
    instrument = Column(String)
    amount = Column(Integer)

    trader_id = Column(Integer, ForeignKey('traders.id'))
    trader = relationship("Trader", backref=backref('open_positions', order_by=id))

    def __init__(self, instrument, amount):
        self.instrument = instrument
        self.amount = amount