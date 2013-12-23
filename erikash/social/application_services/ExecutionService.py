__author__ = 'erik'


class ExecutionService(object):
    def __init__(self, trader_repository):
        """
        @type trader_repository: SqlTraderRepository
        """
        self._trader_repository = trader_repository

    def open_position_for_all_traders(self, instrument, amount):
        all_traders = self._trader_repository.get_all_traders()

        for trader in all_traders:
            trader.open_position(instrument, amount)

        self._trader_repository.commit()