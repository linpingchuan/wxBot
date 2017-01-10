# coding:utf8
import unittest

from src.com.moon.core.MsgType import MsgType


class TestMsgType(unittest.TestCase):
    def setUp(self):
        self.msgType = MsgType()

    def testMsgType(self):
        print(self.msgType.Contact)

if __name__ == '__main__':
    unittest.main()
