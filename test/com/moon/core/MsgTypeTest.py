# coding:utf8
import json
import unittest

from src.com.moon.core.Message import MessageDecorator, Message, User, Content
from src.com.moon.core.MsgType import MsgType


class TestMsgType(unittest.TestCase):
    def setUp(self):
        self.msgType = MsgType()

    def testMsgType(self):
        print(self.msgType.Contact)

    def testJson(self):
        user=User('id','name')
        pass
if __name__ == '__main__':
    unittest.main()
