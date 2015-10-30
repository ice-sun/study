#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing
import getpass
#导入隐藏密码模块

#错误次数
error_times = 0
user_name = 'xiaobing'
password = '123'

#无限验证循环
while True:
    login_name = raw_input('user_name:')
    login_pwd = getpass.getpass('password:')
    #判断用户名密码并且验证错误次数是否小于3
    if login_name.strip() == user_name and login_pwd.strip() == password and error_times <3:
        print u'%s 你好,登陆成功' %user_name
        #正确就跳出循环
        break
    else:
        error_times += 1
        print u'登陆失败'
        if error_times >= 3:
            print u'你已经输错3次，已被锁定'



