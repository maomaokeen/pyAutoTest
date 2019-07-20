#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import getcwd
import os
from logs.log import log1
import time

rq = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取本地时间 转换成日期
sender = 'fantasycat@yeah.net'  # 发件人邮箱
password = 'SQMmaomao0125'  # 发件人邮箱密码
addressed_eamil = '851778331@qq.com'  # 收件人邮箱

path = getcwd.get_cwd()
file = os.path.join(path, 'report/钱东敏测试自动化框架报告.html')  # 测试报告地址


def mail():
    try:
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = formataddr(['发件人姓名', sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        log1.info('发件人邮箱：%s' % sender)
        message['To'] = formataddr(['收件人姓名', addressed_eamil])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        log1.info('收件人邮箱：%s' % addressed_eamil)
        message['Subject'] = rq + "xxxUI自动化测试报告"  # 邮件的主题，也可以说是标题

        # 邮件正文内容
        message.attach(MIMEText('附件为xxxUI自动化测试报告', 'plain', 'utf-8'))

        # 构造附件1
        att1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
        log1.info('读取附件')
        att1["Content-Type"] = 'application/octet-stream'
        # filename是附件名，附件名称为中文时的写法
        att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "钱东敏测试自动化框架报告.html"))
        # 附件名称非中文时的写法
        # att["Content-Disposition"] = 'attachment; filename="test.html")'
        message.attach(att1)
        log1.info('添加附件')

        server = smtplib.SMTP_SSL("smtp.yeah.net", 465)  # 发件人邮箱中的SMTP服务器，ssl端口一般为465， 非ssl一般端口是25
        log1.info('连接yeah邮箱smtp服务')
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        log1.info('连接成功')
        server.sendmail(sender, addressed_eamil, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        log1.info("邮件发送成功")
    except Exception:
        log1.error("邮件发送失败", exc_info=1)
