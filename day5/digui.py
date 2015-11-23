#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing

def func(arg1,arg2):
    if arg1 == 0:
        pass

    arg3 = arg1 + arg2

    if arg3 > 10000:
        return arg3
    return func(arg2,arg3)

result = func(0,1)
print result



func(0,1)