# coding:utf8
import json

from src.com.moon.core.MessageService import MessageService
from src.com.moon.dao.SelfMessageDao import SelfMessageDao


class SelfMessageService(MessageService):
    def execute(self, messageDecorator):
        selfMessageDao=SelfMessageDao()
        selfMessageDao.insertMessage(messageDecorator.msg())
        # msg = '无与伦比，为杰沉沦'
        # self.messageProcessor.processMssage(msg, messageDecorator.user.id)