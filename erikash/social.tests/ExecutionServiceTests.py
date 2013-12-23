import unittest
from mock import Mock
from erikash.social.SqlTraderRepository import SqlTraderRepository
from erikash.social.application_services import ExecutionService
from erikash.social.domain import Trader

__author__ = 'erik'


class ExecutionServiceTests(unittest.TestCase):
    def test_opens_a_position_for_all_traders(self):
        trader = Trader()

        repository = SqlTraderRepository()
        repository.get_all_traders = Mock(return_value=[trader])

        execution_service = ExecutionService(repository)
        execution_service.open_position_for_all_traders("EURUSD", 10000)

        self.assertTrue(("EURUSD", 10000) in trader.open_positions)


if __name__ == '__main__':
    unittest.main()