# -*- coding: UTF-8 -*-
import unittest

import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)


from framework.Base_Page import BasePage
from pageobject.BaiduPage import BaiduPage

import pytest


class test_baidu(unittest.TestCase):
    '''百度首页'''

    def setUp(self):#初始化信息，如启动哪个浏览器
        bro = BasePage(self)
        self.driver = bro.open_browser(0)
    def tearDown(self):
        self.driver.quit()

    def test_baisu(self):
        '''测试百度搜索'''
        baisu = BaiduPage(self.driver)
        baisu.type_kw('selenium')
        baisu.click_su()
        BasePage.my_sleep(3)
        print(baisu.text_nums_text())
        print(baisu.suvalue())
        assert baisu.text_nums_text() =='百度为您找到相关结果约30,700,000个'
        self.assertEqual(baisu.text_nums_text(),'百度为您找到相关结果约30,700,000个')
        BasePage.get_img(self)


if __name__ == '__main__':
    unittest.main()
