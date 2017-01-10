# coding:utf8

class MessageService:
    def __init__(self, messageProcessor):
        '''
        消息服务
        '''
        self.messageProcessor = messageProcessor

    def execute(self, messageDecorator):
        pass
