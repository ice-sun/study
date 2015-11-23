#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing

#查，加，删
#定义读的函数
import os
import json
import time

def fetch(backend):
    #打开文件ha
    with open('ha') as obj:
        flag = False
        #建个空列表，为后续将backend 下的值存储用
        fetch_list = []
        #按行读取文件，每次只读取一行
        for line in obj:
            #如果这行内容等于 backend 参数值，就设置个flage值为True，认为找到了要找的代码块，然后跳出这个循环，读取代码块的下一行内容
            if line.strip() == "backend %s" % backend:
                flag = True
                continue
            #如果这个flag = True 说明已找到代码块，然后将这行内容加入到空列表fetch_list
            if flag and line.strip():
                fetch_list.append(line.strip())
            #如果这个flag = True 说明已找到代码块并且又遇到了backend开头的代码，则说明后面的内容已无关，不需要继续循环
            if line.strip().startswith("backend") and flag:
                break


        return fetch_list


def add_ha(dict_info):
    #获取要添加的 backend值
    backend_title = dict_info.get("backend")
    current_title = "backend %s" % backend_title
    #要添加的backend 的server记录
    server_record_dict = dict_info.get("record")
    current_record = "server %s %s weight %s maxconn %s" %(server_record_dict.get("server"),server_record_dict.get("server"),server_record_dict.get("weight"),server_record_dict.get("maxconn"))
    #获取当前这个backend记录下的server列表
    serverlist = fetch(backend_title)
    #判断这个新增backend 是否存在
    if serverlist:
        #增加server记录
        #打开旧文件，并打开新文件
        with open('ha') as read_obj,open('ha_new',w) as write_obj:
            #设置是否已经读取的标识
            flag = False
            #设置是否写入新记录的标识
            has_write_flage = False
            #读取文件，按行读取
            for line in read_obj:
                #如果读取行到了要写入的backend行，就设置读取标识为Ture，并跳出本次循环，读取下一行
                if line.strip() == current_title:
                    flag = True
                    continue
                #如果已读取到写入行，并且读取到了新的backend记录，就设置flag为False，实现一次写入记录，而不是多次写入覆盖
                if flag and line.strip().startswith("backend"):
                    flag = False
                #通过has_write_flage标识设置是否写入
                if flag:
                    #如果没有写入，则将serverlist中的server记录按条写入到配置文件内
                    if not has_write_flage:
                        for new_line in serverlist:
                            write_obj.write("%s %s \n" %(" "*8,new_line))
                    #
                    else:
                        has_write_flage=True
                else:
                    write_obj.write(line)
    else:
        #增加backend并添加记录
        #打开文件写入新记录，同时打开旧文件和新文件
        with open('ha') as read_obj,open('ha_new','w') as write_obj:
            for line in read_obj:
                write_obj.write(line)
            #这里需要注意加换行，否则会出现新增backend记录加到上一个server记录下
            write_obj.write("\n")
            write_obj.write(current_title+"\n")
            write_obj.write("%s %s \n" %(" "*8,current_record) )
        os.rename('ha','ha.bak.%s' % time.time())
        os.rename('ha_new','ha')

def del_ha(dict_info):
    #获取要删除的backend
    backend_title = dict_info.get("backend")
    current_title = "backend %s" % backend_title
    #要添加的backend 的server记录
    server_record_dict = dict_info.get("record")
    current_record = "server %s %s weight %s maxconn %s" %(server_record_dict.get("server"),server_record_dict.get("server"),server_record_dict.get("weight"),server_record_dict.get("maxconn"))
    #获取当前这个backend记录下的server列表
    serverlist = fetch(backend_title)
    #判断这个删除的backend 下是否存在serverlist
    if not serverlist:
        #不存在就不返回任何任何内容
        return
    else:
        #判断这个要删除的记录是否在serverlist内
        if current_record not in serverlist:
            return
        else:
            #在的话就删除serverlist列表内的这个记录值
            del serverlist[serverlist.index(current_record)]
            #如果删除后这个server记录里还有server值，就把backend_title加到serverlist内，并加到第一个位置
            if len(serverlist) > 0:
                serverlist.insert(0, backend_title)
        #打开旧文件和新文件
        with open('ha') as read_obj,open('ha_new',w) as write_obj:
            #设置是否已经读取的标识
            flag = False
            #设置是否写入新记录的标识
            has_write_flage = False
            #读取文件，按行读取
            for line in read_obj:
                #如果读取行到了要写入的backend行，就设置读取标识为Ture，并跳出本次循环，读取下一行
                if line.strip() == current_title:
                    flag = True
                    continue
                #如果已读取到写入行，并且读取到了backend记录，就设置flag为False，实现一次写入记录，而不是多次写入覆盖
                if flag and line.strip().startswith("backend"):
                    flag = False
                #通过has_write_flage标识设置是否写入
                if flag:
                    #如果没有写入，则将serverlist中的server记录按条写入到配置文件内
                    if not has_write_flage:

                        for new_line in serverlist:
                            #如果记录以backend开头则把这个记录也写入进去，并顶格写入
                            if new_line.startswith('backend'):
                                write_obj.write(new_line+'\n')
                            #如果不是则加入8个空格写入
                            else:
                                write_obj.write("%s %s \n" %(" "*8,new_line))

                    else:
                        has_write_flage=True
                else:
                    write_obj.write(line)
        os.rename('ha','ha.bak.%s' % time.time())
        os.rename('ha_new','ha')


if __name__ == '__main__':

    print '''1、获取server记录
              2、添加server记录
              3、删除server记录
              '''
    num = raw_input('请输入序号：')
    data = raw_input('请输入内容：')
    if num == '1':
        #fetch(data)
        print fetch(data)
    else:
        dict_data = json.loads(data)
        if num == '2':
            add(dict_data)
        elif num == '3':
            remove(dict_data)
        else:
            pass

