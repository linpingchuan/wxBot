# coding:utf8
import jieba


class jieba_service:
    def execute(self,messageDecorator):
        data = messageDecorator.content.data
        seg_list = jieba.cut(data, cut_all=False)
        return list(seg_list)