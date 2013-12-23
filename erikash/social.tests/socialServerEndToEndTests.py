import unittest
from erikash.social.SqlTraderRepository import SqlTraderRepository, InMemoryTraderRepository
from erikash.social.SocialServer import SocialServer
from erikash.social.domain.Trader import Trader

__author__ = 'erik'


class SocialServerEndToEndTests(unittest.TestCase):
    def test_opens_positions_for_all_traders_when_a_position_is_opened(self):
        message_broker_fake = MessageBrokerFake()
        social_server_runner = SocialServerRunner(message_broker_fake)

        message_broker_fake.position_opened("EURUSD", 10000)

        # Assert
        social_server_runner.opened_positions_for_copying_traders("EURUSD", 10000)

if __name__ == '__main__':
    unittest.main()


class SocialServerRunner(object):
    def __init__(self, message_broker_fake):
        self._use_in_memory_db = False

        self.social_server = SocialServer()
        if self._use_in_memory_db:
            self.social_server._trader_repository = InMemoryTraderRepository()

        trader = Trader()
        self.social_server._trader_repository.append(trader)
        self.social_server._message_broker = message_broker_fake

        self.social_server.bootstrap()

    def opened_positions_for_copying_traders(self, instrument, amount):
        if self._use_in_memory_db:
            # Make sure the transaction / unit of work is committed
            trader_repository = self.social_server._trader_repository
        else:
            trader_repository = SqlTraderRepository(self.social_server._session_factory.create_session())

        traders = trader_repository.get_all_traders()

        assert len(traders) > 0

        for trader in traders:
            assert self.has_open_position(trader.open_positions, instrument, amount)

    def has_open_position(self, open_positions, instrument, amount):
        for position in open_positions:
            if position.instrument == instrument and position.amount == amount:
                return True

        return False


class MessageBrokerFake(object):
    def __init__(self):
        self.listeners = list()

    def position_opened(self, instrument, amount):
        for listener in self.listeners:
            listener.position_opened(instrument, amount)


    def subscribe(self, social_server_runner):
        """
        @type social_server_runner: SocialServerRunner
        """
        self.listeners.append(social_server_runner)
