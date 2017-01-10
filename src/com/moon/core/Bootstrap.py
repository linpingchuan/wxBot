# coding:utf8
from src.com.moon.core.ServiceManager import ServiceManager
from src.com.moon.router.MessageDispatcher import MessageDispatcher
from src.com.moon.router.MessageProcessor import MessageProcessor


class Bootstrap:
    '''
    服务启动类
    '''

    def __init__(self, wxBot):
        self.messageProcessor = MessageProcessor(wxBot)
        self.serviceManager = ServiceManager(self.messageProcessor)
        self.messageDispatcher = MessageDispatcher(self.serviceManager)
