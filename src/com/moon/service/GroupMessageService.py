# coding:utf8
from src.com.moon.core.MessageService import MessageService


class GroupMessageService(MessageService):
    def execute(self,messageDecorator):
        msg='无与伦比，为杰沉沦'
        self.messageProcessor.processMssage(msg,messageDecorator.user.id)
