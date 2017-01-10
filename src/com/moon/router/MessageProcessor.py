# coding:utf8

class MessageProcessor:
    '''
    消息处理器
    '''
    def __init__(self,wxbot):
        self.wxbot=wxbot

    def processMssage(self,word,toUserId):
        '''
        消息处理，发送给对应的接收方
        :param word:
        :param toUserId:
        :return:
        '''
        self.wxbot.send_msg_by_uid(word,toUserId)


