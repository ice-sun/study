#!/usr/bin/python
#_*_ coding:utf-8 _*_

customer= raw_input(u'你的名字: ')   #顾客名字
money = int(raw_input(u'你有多少钱购物: '))  #购物余额
sell_list = ['MacbookAir','starbucks coffee','Iphone6 plus']  #购物列表
sell= sell_list
price_list = [7999,33,6188]                 #价格列表
price = price_list
shop_list = []

print u'%s你好,欢迎光临本店,祝你购物愉快' % customer
list = '''
    Welcome the Ice's shopping mall ,bellow are the things we are selling:
    1.%s    %d
    2.%s    %d
    3.%s    %d
    5.exit
    ''' % (sell[0],price[0],sell[1],price[1],sell[2],price[2])
print list      #打印菜单

shop_yes = True
while shop_yes:                 #重复询问是否继续购买
    choose = int(raw_input(u'您要购买什么: ')) - 1
    #print price_list[choose]
    if choose == 4:
        print money
        print u'您已购买的物品',shop_list
        break
    if price_list[choose] < money:
        money = money - price_list[choose]
        shop_list.append(sell_list[choose])
    else :
        print u'您的余额不足'
        for i in list:
            print i



