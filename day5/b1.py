#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing
import index

key = '12345'
ser_list=index.fetch_serverlist('test',token=key)   #4 执行fetch_serlist函数，相当于执行inner函数
print ser_list
#print '---------'
#index.f2('1.1.1.1')

