# -*- coding: UTF-8 -*-
import unittest

import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)


from framework.Base_app import base_app
from framework.Base_Page import BasePage
from pageobject.licai_page import licaiPage
import time


class test_licai(unittest.TestCase):
    '''手机app理财页面'''

    def setUp(self):#appium启动apk
        bro = base_app()
        self.driver = bro.open_apkdriver()

    def tearDown(self):
        self.driver.quit()

    def test_licai(self):
        '''测试理财点击'''

        lp=licaiPage(self.driver)
        time.sleep(30)
        lp.click_licai1()
        lp.know_click()
        print(lp.licai2)



if __name__=="__main__":
    unittest.main()



