#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file:
#@function:-----------

from .model import User
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_

app = Flask(__name__)
#数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql pymysql://root:123456@127.0.0.1/LSYMYSQL'
#追踪修改记录
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#获取连接对象
# db = SQLAlchemy(app,use_native_unicode='utf8')
db = SQLAlchemy()
db.init_app(app)
class Database_Pub(object):
    def __init__(self,da_dict):
        self.user = User()
        self.user.mobile = da_dict.get('mobile',None)
        self.user.first_name = da_dict.get('first_name',None)
        self.user.last_name = da_dict.get('last_name',None)
        self.user.last_time = da_dict.get('last_name',None)
        self.user.otp = da_dict.get('otp',None)
        self.user.access_token = da_dict.get('access_token',None)
        self.user.refresh_token = da_dict.get('refresh_token',None)
        self.user.expiry = da_dict.get('expiry',None)
    #添加
    def add_user(self):
        try:
            db.session.add(self.user)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()
    #查询
    def sel_user(self):
        return  self.user.query.filter(self.user.mobile == self.user.mobile)
    #更新
    def upd_user(self):
        return self.user.query.filter(self.user.mobile == self.user.mobile).all()
    #删除

