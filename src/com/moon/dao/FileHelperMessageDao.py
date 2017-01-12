# coding:utf8
from src.com.moon.conf.MongoConf import DbClient
from src.com.moon.dao.MessageDao import MessageDao


class FileHelperMessageDao(MessageDao):
    def __init__(self):
        self.fileHelperMessage=DbClient.db.file_helper_message

    def insertMessage(self, data):
        result=self.fileHelperMessage.insert_one(data)
        return result

    def queryMessageWithRegex(self, key, value):
        result=self.fileHelperMessage.find({key:{'$regex':value}})
        return result