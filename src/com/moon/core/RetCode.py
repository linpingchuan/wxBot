# coding:utf8

class RetCode:
    def __init__(self):
        '''
            微信返回的通讯码(retcode):
            LOGOUT 1100 -> 从微信客户端上登出
            LOGIN_WEB 1101 -> 从其它设备上登了网页微信
            LOGIN 0   -> 正常登陆
        '''
        self.LOGOUT = 1100
        self.LOGIN_WEB = 1101
        self.LOGIN = 0

class Selector:
    def __init__(self):
        '''
            微信登陆后返回的信息
            NOTHING 0 -> 无事件
            NEW 2 -> 消息
            UNKNOWN 3 -> 未知
            CONTACT_LIST_UPDATE 4 -> 通讯录更新
            RED_ENVELOP 6 -> 可能是红包
            OPERATE_ON_PHONE 7 -> 在手机上操作了微信
        '''
        self.NOTHING = 0
        self.NEW=2
        self.UNKNOWN=3
        self.CONTACT_LIST_UPDATE=4
        self.RED_ENVELOPE=6
        self.OPERATE_ON_PHONE=7
