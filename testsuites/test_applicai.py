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

        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("zhongxinjiantou.szkingdom.android.newphone:id/tv_title").text("理财")').click()
        time.sleep(10)
        a = self.driver.find_element_by_id('zhongxinjiantou.szkingdom.android.newphone:id/financing_titleText').text
        assert a=='理财'
        BasePage.get_img(self)
        time.sleep(10)
        self.driver.find_element_by_android_uiautomator('new UiSelector().description("定期理财")').click()
        time.sleep(10)
        b = self.driver.find_element_by_xpath("//android.widget.TextView[@text='定期理财']").text
        assert b == '定期理财'
        BasePage.get_img(self)

if __name__=="__main__":
    unittest.main()



