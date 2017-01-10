# coding:utf8

class MsgType:
    def __init__(self):
        '''
        处理原始微信消息的内部函数
            msg_type_id:
                0 -> Init
                1 -> Self
                2 -> FileHelper
                3 -> Group
                4 -> Contact
                5 -> Public
                6 -> Special
                99 -> Unknown
        '''
        self.Init=0
        self.Self=1
        self.FileHelper=2
        self.Group=3
        self.Contact=4
        self.Public=5
        self.Special=6
        self.Unknown=99