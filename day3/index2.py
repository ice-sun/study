#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing

read= file('db','r')
user_list=read.readlines()
read.close()

dic={}
for item in user_list:
    item=item.strip()
    line_list = item.split('|')
    dic[line_list[0]]=line_list[1:]


for k,v in dic.items():
    print k,v
#dic = {
#	'alex':[123,1],
#	'eric':[123,1],
#	'tony':[123,1]
#}
