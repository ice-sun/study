#!/usr/bin/python
#-*- coding:utf-8 -*-
#powered by xiaobing

menu = ({'a':{'b':[1,2],'c':[3,4]},'d':{'e':[7,8],'f':[9,10]}})

for i1 in menu.keys():
    print i1
level2 = raw_input('请输入下级菜单： ')