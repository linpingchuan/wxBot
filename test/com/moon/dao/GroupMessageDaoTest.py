# coding:utf8
import json
import unittest

from src.com.moon.dao.GroupMessageDao import GroupMessageDao


class GroupMessageDaoTest(unittest.TestCase):
    def setUp(self):
        self.dao=GroupMessageDao()
    def testInsert(self):
        postData={
            u'author':u'Bill'
        }
        from src.com.moon.core.Message import User
        user=User( u'\u54af\u697c',0)
        print user.__dict__
        result=self.dao.insertMessage(user.__dict__)
        print(result.inserted_id)

    def testQuery(self):
        results=self.dao.queryMessageWithRegex(u'author',u'Bill')
        for result in results:
            print result


if __name__ == '__main__':
    unittest.main()