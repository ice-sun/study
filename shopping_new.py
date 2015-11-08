#!/usr/bin/python
#_*_ coding:utf-8 _*_

#读取用户信息到 user_info_list 中
read = file('db','r+')
user_info_list = read.readlines()
read.close()

#将user_info_list处理成字典{用户名：余额}
user_info_dict = {}
for item in user_info_list:
    user_info = item.split('|')
    user_info_dict = {user_info[0]:int(user_info[1])}


#获取用户名，验证是否在库文件内
    customer= raw_input('你的名字: ')   #顾客名字
    if customer.strip() not in user_info_dict.keys():
        user_info_dict[customer] = int(raw_input('你有多少钱购物: '))  #购物余额

#对应物品价格，这里可以用字典
sell_list = ['MacbookAir','starbucks coffee','Iphone6 plus']  #购物列表
sell= sell_list
price_list = [7999,33,6188]                 #价格列表
price = price_list
shop_list = []

#首次展示菜单
print u'%s你好,欢迎光临本店,祝你购物愉快' % customer
menu_list = '''
    Welcome the Ice's shopping mall ,bellow are the things we are selling:
    1.%s    %d
    2.%s    %d
    3.%s    %d
    5.exit
    ''' % (sell[0],price[0],sell[1],price[1],sell[2],price[2])
print menu_list      #打印菜单

#循环提示购物什么
shop_yes = True
while shop_yes:                 #重复询问是否继续购买
    choose = int(raw_input('您要购买什么: ')) - 1
    #增加退出功能
    if choose == 4:
        print user_info_dict[customer]
        print '您已购买的物品',shop_list
        temp_list=[]
        for key,value in user_info_dict.items():
            temp = "%s|%d"  % (key,value)
            temp_list.append(temp)
        tem_str = '\n'.join(temp_list)
        w_obj = file('db', 'w')
        w_obj.write(tem_str)
        w_obj.close()
        break
    #判断是否买得起，并计算余额
    if price_list[choose] < user_info_dict[customer]:
        user_info_dict[customer] = user_info_dict[customer] - price_list[choose]
        shop_list.append(sell_list[choose])
        temp_list=[]
        for key,value in user_info_dict.items():
            temp = "%s|%d"  % (key,value)
            temp_list.append(temp)
        tem_str = '\n'.join(temp_list)
        w_obj = file('db', 'w')
        w_obj.write(tem_str)
        w_obj.close()

    else :
        print '您的余额不足'
        temp_list=[]
        for key,value in user_info_dict.items():
            temp = "%s|%d"  % (key,value)
            temp_list.append(temp)
        tem_str = '\n'.join(temp_list)
        w_obj = file('db', 'w')
        w_obj.write(tem_str)
        w_obj.close()




