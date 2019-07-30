# -*- coding: UTF-8 -*-
from framework.Base_Page import BasePage


class BaiduPage(BasePage):
    #列出所有元素的定位方法和定位
    kw = ['id', 'kw']  # 搜索输入框
    su = ['css', '#su']  # 搜索按钮
    new = ['link', '新闻'] #新闻按钮
    test=['css','.nums_text'] #统计搜索数量元素

    #对元素进行操作
    def text_nums_text(self):
        a=self.text(self.test)
        return a

    def suvalue(self):
        a=self.valueinfo(self.su, 'id')
        return a


    def type_kw(self, value):
        self.type(self.kw, value)

    def click_su(self):
        self.click(self.su)

    def click_new(self):
        self.click(self.new)

