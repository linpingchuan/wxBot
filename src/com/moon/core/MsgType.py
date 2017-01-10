# coding:utf8

class MsgType:

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
        Init = 0
        Self = 1
        FileHelper = 2
        Group = 3
        Contact = 4
        Public = 5
        Special = 6
        Unknown = 99
