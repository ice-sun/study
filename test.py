#!/usr/bin/python
#-*- coding:utf-8 -*-

user = "xiaobing"
password = "123"

for i in range(3):
    user_input = raw_input('username:')
    password_input = raw_input('password:')

    if user_input == user and password_input == password :
        print "welcome %s come in" %user
        break
    elif user_input == 'guest':
        print 'hi guest '
        break

    else:
        print 'you username is wrong,please try again'
else:
    print "you have tru three times,you will be locked"
