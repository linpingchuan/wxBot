# coding:utf8

from pymongo import *

class DbClient:
    def __init__(self):
        self.client=MongoClient("172.19.5.162",27017)
        self.name='wechat'
        self.db=self.client[self.name]


