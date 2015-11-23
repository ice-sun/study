#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing

def func1(arg):
    return arg+10

#result = func1(100)
#print result
#func2 = lambda a:a+1
#result = func2(1000)
#print result
li = [1,2,3,4]
newlist=map(func1,li)

print newlist

l1=[1,2,3]
l2=[3,4,5]
l3=[4,5,6]
print map(lambda a1,a2,a3:a1+a2+a3,l1,l2,l3)

l4 = [1,44,55,22,11,33]
print filter(lambda a:a>33,l4)

l5 = [1,2,3,4,5,6,7,8,9,10]
print reduce(lambda a1,a2:a1+a2,l5)

