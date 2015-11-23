#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing
'''
def func1():
    yield 1
    yield 2
    yield 3

for i in func1():
    print i
'''

def mrange(arg):
    seed = 0

    while True:

        seed = seed +1
        if seed >10 :
            return
        else:
            yield seed

for i in mrange(10):
    print i