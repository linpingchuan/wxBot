# coding:utf8
import json

from src.com.moon.core.MessageService import MessageService
from src.com.moon.dao.GroupMessageDao import GroupMessageDao


class GroupMessageService(MessageService):
    def execute(self,messageDecorator):
        groupMessageDao=GroupMessageDao()
        messageJson=json.dumps(messageDecorator.msg)
        groupMessageDao.insertMessage(messageJson)
        # self.messageProcessor.processMssage('',messageDecorator.user.id)

