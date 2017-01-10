# coding:utf8
from src.com.moon.service.GroupMessageService import GroupMessageService
from src.com.moon.service.SelfMessageService import SelfMessageService


class ServiceManager:
    '''
        消息服务管理器
    '''
    def __init__(self,messageProcessor):
        self.messageProcessor=messageProcessor
        self.register()

    def register(self):
        self.groupMessageService=GroupMessageService(self.messageProcessor)
        self.selfMessageService=SelfMessageService(self.messageProcessor)

    def groupMessageService(self):
        return self.groupMessageService

    def selfMessageService(self):
        return self.selfMessageService