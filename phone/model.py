#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@time:
#@Author:lsy
#@file:
#@function:-----------
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .database_public import db
# app = Flask(__name__)
# #数据库连接
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql pymysql://root:123456@127.0.0.1/LSYMYSQL'
# #追踪修改记录
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# #获取连接对象
# db = SQLAlchemy(app,use_native_unicode='utf8')
#用户模型
class User(db.Model):
    id = db.Column(db.INT,primary_key=True)  #主键
    mobile = db.Column(db.String(100),unique=True)
    first_name = db.Column(db.String(50),unique=True)
    last_name = db.Column(db.String(100),unique=True)
    access_time = db.Column(db.DateTime)
    refresh_time = db.Column(db.DateTime)
    otp_time = db.Column(db.DateTime)
    otp = db.Column(db.String(100))
    access_token = db.Column(db.String(255))
    refresh_token = db.Column(db.String(255))
    expiry = db.Column(db.INT)

    __tablename__ = 'user_information'
    def __repr__(self):
        return 'User {0}'.format(self.mobile)

