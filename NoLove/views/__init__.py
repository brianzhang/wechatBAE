#coding=utf-8
#-*- coding: utf-8 -*-

from bae.api import logging
from xml.etree import ElementTree as ET
from flask import request, jsonify, make_response
from NoLove.configs import settings
run_log = logging.getLogger('run_loggin')
def parse_msg():
    #"parse the command sent from wechat"
    recvmsg = request.data 
    root = ET.fromstring(recvmsg)
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    return msg
 
def set_content(msg=None):
    try:
        run_log.debug('msg_content:'+msg)
        content = settings.MSG[msg]
    except Exception, e:
        if msg:
            content = settings.MSG['__error__msg__'] % (msg)
        else:
            content = settings.MSG['__system__msg__']
    return content