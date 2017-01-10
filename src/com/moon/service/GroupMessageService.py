# coding:utf8
from src.com.moon.core.Message import MessageDecorator


class GroupMessageService:
    '''
        群消息服务
    '''
    def __init__(self,messageProcessor):
        self.messageProcessor=messageProcessor

    def execute(self,messageDecorator):
        msg='无与伦比，为杰沉沦'
        self.messageProcessor.processMssage(msg,messageDecorator.user.id)
