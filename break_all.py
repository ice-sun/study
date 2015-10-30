#/usr/bin/python
#_*_ coding:utf-8 _*_
import time
loop1 = 0
loop2 = 0

while True:
    loop1 +=1
    print 'loop1=',loop1
    break_flag = False
    time.sleep(1)
    while True:
        loop2 +=1
        if loop2 ==5:
            break_flag = True
            break
        time.sleep(1)
        print 'loop2=',loop2
    if break_flag:
        print u'子循环已跳出，父也要跳'
        break
