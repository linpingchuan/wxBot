# coding:utf8
from src.com.moon.core.Message import MessageDecorator
from src.com.moon.core.MsgType import MsgType
from src.com.moon.service.GroupMessageService import GroupMessageService


class MessageDispatcher:
    '''
    消息分发器
    '''

    def __init__(self, serviceManager):
        '''
        初始化服务管理器
        :param serviceManager:
        '''
        self.serviceManager = serviceManager

    def dispatch(self, msg):
        '''
        对消息进行包裹，并进行分发
        :param msg:
        :return:
        '''
        self.messageDecorator = MessageDecorator(msg)
        if self.messageDecorator.message.msgTypeId == MsgType.Contact:
            pass
        elif self.messageDecorator.message.msgTypeId == MsgType.Group:
            self.serviceManager.groupMessageService.execute(self.messageDecorator)
        elif self.messageDecorator.message.msgTypeId == MsgType.Self:
            self.serviceManager.selfMessageService.execute(self.messageDecorator)
        elif self.messageDecorator.message.msgTypeId == MsgType.FileHelper:
            self.serviceManager.fileHelperMessageService.execute(self.messageDecorator)
        elif self.messageDecorator.message.msgTypeId == MsgType.Contact:
            self.serviceManager.contactMessageService.execute(self.messageDecorator)
