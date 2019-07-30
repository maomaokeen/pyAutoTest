# -*- coding: UTF-8 -*-
from selenium import webdriver
from framework.Base_Page import BasePage
import os

abspath = os.path.abspath(r"F:\m2\chromedriver.exe")
dr = webdriver.Chrome(abspath)
dr.get("https:www.baidu.com")
s = dr.window_handles
driver = BasePage(dr)
kw = ['id','kw']
driver.type(kw,'selenium+python')
driver.my_sleep(3)
test=['css','.nums_text']
a=driver.text(test)
print(a)
driver.implicitly_wait(2)
driver.type(kw,'selenium')
su = ['id','su']
driver.click(su)
driver.get_img()
driver.my_sleep(2)
driver.get_title()
