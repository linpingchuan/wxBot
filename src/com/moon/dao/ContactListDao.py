# coding:utf8
from src.com.moon.conf.MongoConf import DbClient
from src.com.moon.dao.MessageDao import MessageDao


class ContactListDao(MessageDao):
    def __init__(self):
        self.contactList = DbClient.client.contact_list

    def insertMessage(self, data):
        result = self.contactList.insert_one(data)
        return result

    def queryMessageWithRegex(self, key, value):
        result = self.contactList.find({key: {'$regex': value}})
        return result
