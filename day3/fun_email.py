#!/usr/bin/env python
#-*- coding:utf-8 -*-
# powered by  xiaobing
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def email(message):
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = formataddr(["武沛齐",'wptawy@126.com'])
    msg['To'] = formataddr(["走人",'424662508@qq.com'])
    msg['Subject'] = "小兵测试"
    server = smtplib.SMTP("smtp.126.com", 25)
    server.login("wptawy@126.com", "WW.3945.59")
    server.sendmail('wptawy@126.com', ['424662508@qq.com',], msg.as_string())
    server.quit()

if __name__== '__main__':
    cpu = 100
    disk = 95
    raw = 50
    for i in range(1):
        if cpu > 90:
            alert = 'cpu is warning'
            email(alert)
        if disk > 90:
            alert = 'disk if almost full warnning'
            email(alert)
        if raw > 90:
            alert = 'raw is warnning '
            email(alert)