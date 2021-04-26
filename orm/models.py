#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'caizhixiang'

import time

from orm.orm import Model,IntegerField, StringField, BooleanField, FloatField, TextField


class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    # created_at = FloatField(default=time.time)
