# coding:utf8
import jieba as jieba

from src.com.moon.core.MessageService import MessageService


class jieba_service(MessageService):
    def execute(self, messageDecorator):
        data=messageDecorator.content.data
        seg_list=jieba.cut(data,cut_all=False)
        return "".join(seg_list)
        pass

