# -*- coding: UTF-8 -*-
from Config.config import Config

#可以写入初始化数据以及浏览器引擎
section = 'selenium'
username = '测试'
password = '一下'



a=Config.config_read('DB', 'dbhost')

print(a)

