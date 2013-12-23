from erikash.social.domain.Trader import Trader

__author__ = 'erik'


class SqlTraderRepository(object):
    def __init__(self, session):
        self._session = session

    def get_all_traders(self):
        return self._session.query(Trader).all()

    def append(self, trader):
        self._session.add(trader)

    def commit(self):
        self._session.commit()


class InMemoryTraderRepository(object):
    def __init__(self):
        self._traders = []

    def get_all_traders(self):
        return self._traders

    def append(self, trader):
        self._traders.append(trader)

    def commit(self):
        pass