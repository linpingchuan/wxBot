# coding:utf-8

from src.com.moon.core.MessageService import MessageService


class ContactMessageService(MessageService):
    def execute(self, messageDecorator):
        self.messageProcessor.wxbot.contact_list

