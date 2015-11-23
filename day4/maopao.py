#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing

li = [11,1,22,5,10]

print li


for n in range(1,len(li)):
    for m in range(len(li) -n) :
        num1 = li[m]
        #获取第m个值
        num2 = li[m+1]
        #获取第m+1个值
        #如果左边比右边大，值互换
        if num1 > num2:
            temp = li[m]
            li[m] = num2
            li[m+1] = temp

print li


