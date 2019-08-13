# -*- coding: UTF-8 -*-
import configparser

from Config.config import Config
from logs.log import log1
import getcwd
import os
import time
from appium import webdriver


path = getcwd.get_cwd()
config_path = os.path.join(path, 'Config/config.ini')
config = configparser.ConfigParser()
config.read(config_path,encoding="utf-8-sig")



class base_app():
    """appium基类"""
    def __init__(self):
        platformName=Config.config_read('appium', 'platformName')
        deviceName=Config.config_read('appium', 'deviceName')
        platformVersion=Config.config_read('appium', 'platformVersion')
        apkpath = Config.config_read('appium', 'app')
        appPackage = Config.config_read('appium', 'appPackage')
        appActivity = Config.config_read('appium', 'appActivity')
        path = getcwd.get_cwd()
        apk_path = os.path.join(path, apkpath)
        desired_caps = {
            'platformName': platformName,
            'deviceName': deviceName,  # 手机设备名称，通过adb devices查看
            'platformVersion': platformVersion,  # android系统的版本号
            'app': apk_path,
            'appPackage': appPackage,  # apk包名
            'appActivity': appActivity,  # apk的launcherActivity
            'noRset':'true',
            'automationNname':'uiautomator2'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3)

    def open_apkdriver(self):
        return self.driver
