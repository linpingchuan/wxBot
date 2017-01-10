# coding:utf8
from src.com.moon.service.GroupMessageService import GroupMessageService


class ServiceManager:
    '''
        消息服务管理器
    '''
    def __init__(self,messageProcessor):
        self.messageProcessor=messageProcessor
        self.register()

    def register(self):
        self.groupMessageService=GroupMessageService(self.messageProcessor)

    def groupMessageService(self):
        return self.groupMessageService