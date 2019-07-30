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
class BasePage:
    """测试基类"""

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def isdisplayed(element):
        """元素是否存在"""
        value = element.is_displayed()
        return value

    @staticmethod
    def my_sleep(secondes):
        """强制等待"""
        time.sleep(secondes)
        log1.info('暂停%d秒' % secondes)

    def implicitly_wait(self, times):
        """隐式等待"""
        self.driver.implicitly_wait(times)
        log1.info('隐式等待%d秒' % times)

    def get_img(self):
        """截图"""
        path = os.path.join(getcwd.get_cwd(), 'screenshots/')  # 拼接截图保存路径
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 按格式获取当前时间
        screen_name = path + rq + '.png'  # 拼接截图文件名
        # noinspection PyBroadException
        try:
            self.driver.get_screenshot_as_file(screen_name)
            log1.info("截图保存成功")
        except BaseException:
            log1.error("截图失败", exc_info=1)

    def open_browser(self,driver):
        browser = driver
        log1.info('读取浏览器配置')
        url = Config.config_read('test', 'url')
        log1.info('读取url：%s' % url)
        try:
            if browser == 0:
                abspath = os.path.abspath(r"F:\m2\chromedriver.exe")
                self.driver = webdriver.Chrome(abspath)
                log1.info('打开的浏览器为chrome')
            elif browser == 1:
                #abspath = os.path.abspath(r"F:\m2\chromedriver.exe")
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

    def find_element(self, selector):
        """定位元素"""
        by = selector[0]
        value = selector[1]
        element = None
        if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
            # noinspection PyBroadException
            try:
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                else:
                    log1.error('没有找到元素')
                log1.info('元素定位成功。定位方式：%s，使用的值%s：' % (by, value))
                return element
            except NoSuchElementException:
                log1.error("报错信息：", exc_info=1)
                self.get_img()  # 调用截图
        else:
            log1.error('输入的元素定位方式错误')

    def type(self, selector, value):
        """输入内容"""
        element = self.find_element(selector)
        element.clear()
        log1.info('清空输入内容')
        # noinspection PyBroadException
        try:
            element.send_keys(value)
            log1.info('输入的内容：%s' % value)
        except BaseException:
            log1.error('内容输入报错', exc_info=1)
            self.get_img()

    def click(self, selector):
        """点击元素"""
        element = self.find_element(selector)
        # noinspection PyBroadException
        try:
            element.click()
            log1.info('点击元素成功')
        except BaseException:
            display = self.isdisplayed(element)
            if display is True:
                self.my_sleep(3)
                element.click()
                log1.info('点击元素成功')
            else:
                self.get_img()
                log1.error('点击元素报错', exc_info=1)

    def text(self, selector):
        """获取文本"""
        text = self.find_element(selector).text
        log1.info('元素的内容是:%s' % text)
        return text

    def valueinfo(self, selector,value):
        """获取元素属性"""
        value_info = self.find_element(selector).get_attribute(value)
        log1.info('元素的%s是%s' % (value,value_info))
        return value_info

    def use_js(self, js):
        """调用js"""
        # noinspection PyBroadException
        try:
            self.driver.execute_script(js)
            log1.info('js执行成功，js内容为：%s' % js)
        except BaseException:
            log1.error('js执行报错', exc_info=1)

    def switch_menue(self, parentelement, secelement, targetelement):
        """三级菜单切换"""
        self.my_sleep(3)
        # noinspection PyBroadException
        try:
            self.driver.switch_to_default_content()
            self.click(parentelement)
            log1.info('成功点击一级菜单：%s' % parentelement)
            self.click(secelement)
            log1.info('成功点击二级菜单：%s' % secelement)
            self.click(targetelement)
            log1.info('成功点击三级菜单：%s' % targetelement)
        except BaseException:
            log1.error('切换菜单报错', exc_info=1)

    def switch_ifarme(self, selector):
        """切换farm"""
        element = self.find_element(selector)
        # noinspection PyBroadException
        try:
            self.driver.switch_to.frame(element)
            log1.info('切换frame成功')
        except BaseException:
            log1.error('切换frame报错', exc_info=1)

    def get_title(self):
        """获取title"""
        title = self.driver.title
        log1.info('当前窗口的title是:%s' % title)
        return title

    def my_quit(self):
        """关闭浏览器"""
        self.driver.quit()
        log1.info('关闭浏览器')

