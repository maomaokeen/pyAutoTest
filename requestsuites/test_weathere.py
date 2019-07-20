import unittest
from logs.log import log1
from framework.Base_requests import test_requests
from Config.config import Config


class weathere(unittest.TestCase):

    def test_weather(self):
        '''查询天气'''
        case_name = '查询天气'
        log1.info("执行测试用例：%s" % case_name)
        try:
            weather = test_requests()  # 初始化测试基类的实例
            url = Config.config_read('weathere', 'url')  # 获取配置文件中的url
            city = Config.config_read('weathere', 'city')  # 获取配置文件中的crty
            status_code, response_json, reurl = weather.get(url+city)  # 调用封装的get方法，接收状态码和相应内容
            message = weather.getdict(response_json, 'message')  # 调用迭代字典方法，获得message字段的值
            test1 = self.assertEqual(status_code, 200)  # 断言状态码等于200
            print(test1)
            test2 = self.assertEqual(message, 'Success !')  # 断言message字段的值等于'Success !'
            print(test2)
            if test1 == None and test2 == None:  # 如果两个断言结果都等于None
                log1.info("测试通过")
        except BaseException as f:
            log1.error("测试用例执行出错: %s" % case_name, exc_info=1)
            raise