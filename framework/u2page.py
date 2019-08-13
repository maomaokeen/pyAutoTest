# -*- coding: UTF-8 -*-
import configparser

from Config.config import Config
from logs.log import log1
from selenium.common.exceptions import NoSuchElementException
import getcwd
import os
import time
from selenium import webdriver


path = getcwd.get_cwd()
config_path = os.path.join(path, 'Config/config.ini')
config = configparser.ConfigParser()
config.read(config_path,encoding="utf-8-sig")

#定义所有的方法，包括driver的启动，元素的定位findelement，元素的操作方法，判断元素是否存在，等待时间，截图
class u2page:
    """测试基类"""

    def __init__(self, d):
        self.d = d

    def find_element(self,element):
        el=self.d(text=element)
        return el

    def click(self,element):
        el=self.find_element(element)
        el.click()
        self.screenshot(1)

    def screenshot(self,open):
        if open==1:
            return self.d.screenshot("iji.png")


