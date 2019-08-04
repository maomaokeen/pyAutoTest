# -*- coding: UTF-8 -*-
import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

import unittest
from framework.Base_Page import BasePage
from pageobject.baidu_new_page import NewPage
from pageobject.BaiduPage import BaiduPage
import pytest


class Test_baidu_new(unittest.TestCase):
    '''百度新闻'''

    def setUp(self):
        bro = BasePage(self)
        self.driver = bro.open_browser()

    @pytest.mark.baidu
    def test_new(self):
        '''搜索selenium'''
        baidu = BaiduPage(self.driver)
        baidu.click_new()
        new = NewPage(self.driver)
        new.type_ww('selenium')
        new.click_wr()


if __name__ == '__main__':
    unittest.main()