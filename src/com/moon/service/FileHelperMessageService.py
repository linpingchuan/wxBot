# coding:utf8
import json

from src.com.moon.core.MessageService import MessageService
from src.com.moon.dao.FileHelperMessageDao import FileHelperMessageDao


class FileHelperMessageService(MessageService):
    def execute(self, messageDecorator):
        fileHelperMessageDao=FileHelperMessageDao()
        messageJson=json.dumps(messageDecorator.msg())
        fileHelperMessageDao.insertMessage(messageJson)