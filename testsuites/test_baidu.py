# -*- coding: UTF-8 -*-
import unittest
from framework.Base_Page import BasePage
from pageobject.BaiduPage import BaiduPage


class test_baidu(unittest.TestCase):
    '''百度首页'''

    def setUp(self):
        bro = BasePage(self)
        self.driver = bro.open_browser()

    def test_baisu(self):
        '''测试百度搜索'''
        baisu = BaiduPage(self.driver)
        baisu.type_kw('selenium')
        baisu.click_su()
        baisu.get_img()
        baisu.my_quit()


if __name__ == '__main__':
    unittest.main()
