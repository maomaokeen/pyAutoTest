from selenium import webdriver
from logs.log import log1
from Config.config import Config
import os


class base_browser():
    def __init__(self, driver):
        self.driver = driver


    def open_browser(self,browser):
        log1.info('读取浏览器配置')
        url = Config.config_read('test', 'url')
        log1.info('读取url：%s' % url)
        try:
            if browser == 0:
                abspath = os.path.abspath(r"F:\m2\chromedriver.exe")
                self.driver = webdriver.Chrome(abspath)
                log1.info('打开的浏览器为chrome')
            elif browser == 1:
                # abspath = os.path.abspath(r"F:\m2\chromedriver.exe")
                self.driver = webdriver.Firefox()
                log1.info('打开的浏览器为Firefox')
            elif browser == 2:
                # abspath = os.path.abspath(r"F:\m2\chromedriver.exe")
                self.driver = webdriver.ie()
                log1.info('打开的浏览器为ie')
            self.driver.get(url)
            self.driver.maximize_window()
            log1.info('浏览器最大化')
            self.driver.implicitly_wait(10)
            log1.info('设置静态等待时间10秒')
            return self.driver
        except BaseException:
            log1.error('浏览器打开报错')
