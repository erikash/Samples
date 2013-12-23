__author__ = 'erik'


class MessageBrokerDispatcher(object):
    def __init__(self, execution_service):
        self._execution_service = execution_service

    def position_opened(self, instrument, amount):
        self._execution_service.open_position_for_all_traders(instrument, amount)