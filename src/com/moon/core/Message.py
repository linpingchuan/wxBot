# coding:utf8

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Content:
    def __init__(self, type, data):
        '''
        content_type_id:
                    0 -> Text
                    1 -> Location
                    3 -> Image
                    4 -> Voice
                    5 -> Recommend
                    6 -> Animation
                    7 -> Share
                    8 -> Video
                    9 -> VideoCall
                    10 -> Redraw
                    11 -> Empty
                    99 -> Unknown
        :param type: 消息类型id
        :param data: 消息结构体
        '''
        self.type = type
        self.data = data


class Message:
    def __init__(self, msgTypeId, msgId, content, toUserId, user):
        self.msgTypeId = msgTypeId
        self.msgId = msgId
        self.content = content
        self.toUserId = toUserId
        self.user = user


class MessageDecorator:
    def __init__(self, msg):
        '''
            消息内容装饰器
        :param msg:
        '''
        contentType = msg['content']['type']
        contentData = msg['content']['data']
        self.content = Content(contentType, contentData)

        userId = msg['user']['id']
        userName = msg['user']['name']
        self.user = User(userId, userName)

        msgTypeId = msg['msg_type_id']
        msgId = msg['msg_id']
        toUserId = msg['to_user_id']
        self.message = Message(msgTypeId, msgId, self.content, toUserId, self.user)

    def msg(self):
        dict = {'content': self.message.content.__dict__, 'user': self.message.content.__dict__,
                'msgTypeId': self.message.msgTypeId, 'msgId': self.message.msgId,
                'toUserId': self.message.toUserId}
        return dict


class ContentType:
    def __init__(self):
        '''
        content_type_id:
                    0 -> Text
                    1 -> Location
                    3 -> Image
                    4 -> Voice
                    5 -> Recommend
                    6 -> Animation
                    7 -> Share
                    8 -> Video
                    9 -> VideoCall
                    10 -> Redraw
                    11 -> Empty
                    99 -> Unknown
        '''
        self.TEXT = 0
        self.LOCATION = 1
        self.IMAGE = 3
        self.VOICE = 4
        self.RECOMMEND = 5
        self.ANIMATION = 6
        self.SHARE = 7
        self.VIDEO = 8
        self.VIDEO_CALL = 9
        self.REDRAW = 10
        self.EMPTY = 11
        self.UNKNOWN = 99
