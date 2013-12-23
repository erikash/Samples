from erikash.social.MessageBrokerDispatcher import MessageBrokerDispatcher
from erikash.social.SessionFactory import SessionFactory
from erikash.social.SqlTraderRepository import SqlTraderRepository
from erikash.social.application_services.ExecutionService import ExecutionService

__author__ = 'erik'


class SocialServer(object):
    def __init__(self):
        self._session_factory = SessionFactory()
        self._trader_repository = SqlTraderRepository(self._session_factory.create_session())
        self._execution_service = None
        self._message_broker = None

    def bootstrap(self):
        self._execution_service = ExecutionService(self._trader_repository)

        dispatcher = MessageBrokerDispatcher(self._execution_service)
        self._message_broker.subscribe(dispatcher)


