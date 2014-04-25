#coding=utf-8
#-*- coding: utf-8 -*-

import os
import random
import urllib2
import hashlib, time, re
import sys
from xml.etree import ElementTree as ET
from bae.core import const
from bae.api import bcs

reload(sys)
sys.setdefaultencoding("utf-8")
from flask import request, render_template, jsonify, g, Blueprint, Response, make_response
from NoLove.configs import settings
from NoLove.views import parse_msg, set_content

nolove_view = Blueprint('nolove', __name__)

@nolove_view.route("/", methods=["POST", "GET"])
def check_signature():
    args = request.args if request.method == 'GET' else request.form
    if request.method == 'GET':
        token = settings.TOKEN #set your token here
        signature = args.get('signature', None)  
        timestamp = args.get('timestamp', None)
        nonce = args.get('nonce', None)
        echostr = args.get('echostr', None)
        tmpList = [token, timestamp, nonce]
        tmpList.sort()
        tmpstr = "%s%s%s" % tuple(tmpList)
        hashstr = hashlib.sha1(tmpstr).hexdigest()
        if hashstr == signature:
            return echostr
        else:
            return 'false'
    else:
        msg = parse_msg()
        try:
            content = set_content(msg["Content"])
        except Exception, e:
            content = settings.MSG['__system__msg__']
        
        echostr = settings.TEXT_TEMP % ( msg['FromUserName'], msg['ToUserName'], str(int(time.time())), content)
        return echostr
        
@nolove_view.route("/index/")
def index():
    resp = make_response(render_template("index.html"))
    return resp
  
@nolove_view.route("/upload", methods=['POST'])
def upload():
	return False