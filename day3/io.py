#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing

obj= open('db','r+')
#obj.seek(5)
print obj.tell()
print obj.read()
print obj.tell()
obj.close()