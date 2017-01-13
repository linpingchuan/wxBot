# coding:utf8
import json

from src.com.moon.core.MessageService import MessageService
from src.com.moon.dao.FileHelperMessageDao import FileHelperMessageDao
from src.com.moon.nlp.jieba_service import jieba_service


class FileHelperMessageService(MessageService):
    def execute(self, messageDecorator):
        fileHelperMessageDao=FileHelperMessageDao()
        messageJson=json.dumps(messageDecorator.msg())
        fileHelperMessageDao.insertMessage(messageJson)
        self.messageProcessor.wxbot.send_msg_by_uid(jieba_service().execute(messageDecorator),self.messageProcessor.wxbot[])
        self.messageProcessor.wxbot.send_msg_by_uid(jieba_service().execute(messageDecorator), '')
