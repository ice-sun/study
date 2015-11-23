#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing
import collections,json



#conf_dic = collections.OrderedDict()
#for i in conf_list:
 #   conf_info = i.strip().split(" ")
  #  if len(conf_info) > 1:
   #     conf_dic[conf_info[0]] = conf_info[1]

def read_ha(*args,**kwargs):

    with open('ha.conf','r') as read:
        conf_list = read.readlines()
    newlist = []
    for i in conf_list:
        newlist.append(i.strip())
    p = newlist.index(*args,**kwargs)
    print newlist[p+1]

def add_ha(*args,**kwargs):
    with open('ha.conf','r') as read:
        conf_list = read.readlines()
        

def del_ha(*args,**kwargs):
     with open('ha.conf','r') as read:
        conf_list = read.readlines()



if __name__ == '__main__':
    while True:
        print '''
    1. 查看 当前配置
    2. 增加ha配置
    3. 删除ha配置
     '''
        choose = int(raw_input('请输入操作： '))
        if choose == 1:
        domain1 = raw_input('请输入backend: ')
        read_ha("backend "+domain1)
    elif choose == 2:
        domain2 = raw_input('请输入backend: ')
        add_ha("backend "+domain2)
    elif choose == 3:
        domain3 = raw_input('请输入backend: ')
        del_ha("backend "+domain3)