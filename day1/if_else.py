#!/usr/bin/python
#-*- coding:utf-8 -*-

#获取用户名
'''name = raw_input('请输入用户名密码：')

if name == 'alex':
    print 'NB'
elif name == 'xiaobing':
    print 'cai niao'
elif name == 'wenqiang':
    print 'qiang ge'
else:
    print 'who are you '
'''
import getpass
name = raw_input('you name:')
pwd = getpass.getpass('you password')

if name == 'alex' and pwd == '123':
    
    print 'login success'
else:
    print 'you name or pwd is wrong'