#coding=utf-8
#-*- coding: utf-8 -*-
from bae.core import const
from bae.api import bcs

DEBUG = True

UPLOAD_FOLDER = '/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

HOST = const.BCS_ADDR
AK = const.ACCESS_KEY
SK = const.SECRET_KEY

TOKEN = 'NOLOVEBYBRIAN'
BUCKET_NAME = 'nolove'

TEXT_TEMP = """<xml>
                 <ToUserName><![CDATA[%s]]></ToUserName>
                 <FromUserName><![CDATA[%s]]></FromUserName>
                 <CreateTime>%s</CreateTime>
                 <MsgType><![CDATA[text]]></MsgType>
                 <Content><![CDATA[%s]]></Content>
                 <FuncFlag>0</FuncFlag>
            </xml>"""

IMG_TEMP = """<xml>
			<ToUserName><![CDATA[%s]]></ToUserName>
			<FromUserName><![CDATA[%s]]></FromUserName>
			<CreateTime>%s</CreateTime>
			<MsgType><![CDATA[news]]></MsgType>
			<ArticleCount>1</ArticleCount>
			<Articles>
				<item>
					<Title><![CDATA[%s]]></Title> 
					<Description><![CDATA[%s]]></Description>
					<PicUrl><![CDATA[%s]]></PicUrl>
					<Url><![CDATA[%s]]></Url>
				</item>
			</Articles>
		</xml>"""
MSG = {
       '__error__msg__': u'抱歉，您传达给我的指令 "%s" 我这傻傻的脑袋没有搜索到耶，没关系我马上去升级我的智慧。',
       '__system__msg__': u"谢谢您关注-木有爱/::) \r我将为你提供生活，工作，情感问题的系列帮助，为你带来快乐，有什么困扰就给我留言吧!/:love \r\r觉得我可爱就介绍给你的朋友圈吧。/:#-0\r\r您还可以给我提供改进意见哟！\r\r如果你不喜欢我请让我你开你的生活圈，我只能说sorry，没能给你提供更好的服务！/:P-(\r\r木有爱真心希望给您带来快乐每一天。/::>",
       u'左颖娜': u'嘿嘿，左颖娜是谁ING？你猜猜吧',
       u'我爱你': u'人家害羞了，我不能爱你。',
       u'你是傻逼': u'都没你傻啊',
       u'傻逼': u'我也和你一样这么认为。',
       'hi': u'hello, 需要我的帮助吗？',
       u'寂寞了': u'想必你应该去玩LOL了',
       u'/::)': u'您好哇，你可以输关键字：笑话，生活，情感，提问 向我获取服务哟！',
       u'/::~': u'亲您怎么了，为何伤心呀？',
       u'/::B': u'/::*您好哇，美女',
       u'你好': u'您好！',
       u'您好': u'您好！',
       u'妈卖批': u'这样真的不好。',
       u'/:P-(': u'亲爱的，你这是怎么了？',
       u'/:<W>': u'嗯，多吃水果对身体好哟，/::P',
       u'我靠': u'借你一个结实的肩膀',
       u'我操': u'请带上你的家伙到指定地点去吧，对了一定要注意安全/::Z',
       u'我不爱你': u'暮然回首，我依旧在为你守候/::$',
       u'::Q': u'汉子我们一起吧 ::Q'
    }