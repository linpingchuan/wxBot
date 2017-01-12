# coding:utf8
from src.com.moon.conf.MongoConf import DbClient
from src.com.moon.dao.MessageDao import MessageDao


class GroupMessageDao(MessageDao):
    def __init__(self):
        self.group_message=DbClient.db.group_message
    def insertMessage(self,data):
        result=self.group_message.insert_one(data)
        return result

    def queryMessageWithRegex(self,key,value):
        result=self.group_message.find({key:{'$regex':value}})
        return result