# coding:utf8

from pymongo import *


class DbClient:
    client = MongoClient("172.19.5.162", 27017)
    name = 'wechat'
    db = client[name]
