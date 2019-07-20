# -*- coding: UTF-8 -*-
from framework.Base_Page import BasePage


class NewPage(BasePage):
    ww = ['id', 'ww']
    wr = ['id', 's_btn_wr']

    def type_ww(self, value):
        self.type(self.ww, value)

    def click_wr(self):
        self.click(self.wr)