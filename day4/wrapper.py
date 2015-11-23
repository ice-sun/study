#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing

def wrapper(func):
    if login("xiaobin"):
        return func
    else:
        print '未认证'
def login(user):
    if user == 'xiaobing':
        return True
    else:
        print 'error name '
@wrapper
def home():
    print 'home'

@wrapper
def shop():
    print 'shop'

def over():
    print 'over'


#home = wrapper(home)
home()
shop()