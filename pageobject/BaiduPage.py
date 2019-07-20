# -*- coding: UTF-8 -*-
from framework.Base_Page import BasePage


class BaiduPage(BasePage):
    kw = ['id', 'kw']  # 搜索输入框
    su = ['id', 'su']  # 搜索按钮
    new = ['link', '新闻']

    def type_kw(self, value):
        self.type(self.kw, value)

    def click_su(self):
        self.click(self.su)

    def click_new(self):
        self.click(self.new)