# coding:utf8
from src.com.moon.conf.MongoConf import DbClient
from src.com.moon.dao.MessageDao import MessageDao


class SelfMessageDao(MessageDao):
    def __init__(self):
        self.self_message=DbClient.db.self_message

    def insertMessage(self, data):
        result=self.self_message.insert_one(data)
        return result

    def queryMessageWithRegex(self, key, value):
        result=self.self_message.find({key:{'$regex':value}})
        return result
