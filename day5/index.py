#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing

#装饰器

#过程：
'''
def auth(func):  #2  func = f1
    def inner(): #4 加载inner
        print 'before'  #5 执行inner
        func()   #6 执行f1，并执行了inner中的验证
    return inner  #3 f1=inner

def auth_arg(func):  #2  func = f1
    def inner(arg): #4 加载inner
        print 'before'  #5 执行inner
        func(arg)   #6 执行f1，并执行了inner中的验证
    return inner  #3 f1=inner
'''
def login(key):      #8 开始执行login函数
    server_key = '12345'  #本地key值

    if server_key == key:  #9 如果客户端key值和server端一样
        return True
    else:
        return False

def auth(func):  #2  func = fetch_serverlist
    def inner(*args,**kwargs): #5 fetch_serverlist(arg,kwargs)   inner函数将从客户端获取的参数传入
        key = kwargs.pop('token')  #6 获取key值，并且将客户端获取的key值从参数中删除
        is_login = login(key)  #7 将获取的key传入login并执行login函数
        if not is_login:
            return 'invild name'

        print 'fetch_serverlist'
        temp = func(*args,**kwargs)   #6 执行f1，并执行了inner中的验证
        print 'after'
        return temp
    return inner  #3 fetch_serverlist=inner

@auth     #1 相当于执行auth(fetch_serverlist)
def fetch_serverlist(arg):
    serverlist = [1,2,3,4]
    return serverlist

#@auth
#def f2(arg):
#    print 'f2',arg


'''
f1 = auth(f1) #1 执行f1的赋值
f1()
'''