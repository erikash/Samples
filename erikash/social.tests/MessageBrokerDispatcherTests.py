import unittest
from mock import Mock
from erikash.social.MessageBrokerDispatcher import MessageBrokerDispatcher

__author__ = 'erik'


class MessageBrokerDispatcherTests(unittest.TestCase):
    def test_invokes_execution_service_when_a_position_is_opened(self):
        execution_service = Mock()
        dispatcher = MessageBrokerDispatcher(execution_service)

        dispatcher.position_opened("EURUSD", 10000)

        execution_service.open_position_for_all_traders.assert_called_once_with("EURUSD", 10000)


if __name__ == '__main__':
    unittest.main()