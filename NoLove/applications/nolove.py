#coding=utf-8
#-*- coding: utf-8 -*-
from flask import Flask
from NoLove.configs import settings
from NoLove.views.nolove import nolove_view
from bae.core.wsgi import WSGIApplication

def create_app(debug=settings.DEBUG):
    app = Flask(__name__, template_folder='../templates/', static_folder="../static")
    app.register_blueprint(nolove_view)
    app.config['UPLOAD_FOLDER'] = settings.UPLOAD_FOLDER
    app.secret_key = 'PS#yio`%_!((f_or(%)))s'
    app.debug = debug
    return app 

app = create_app(settings.DEBUG)
application = WSGIApplication(app, stdout="log", stderr="log")
