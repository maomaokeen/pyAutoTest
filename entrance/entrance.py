# -*- coding: UTF-8 -*-
import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

import testsuites.test_baidu
import testsuites.test_baidu_new
import requestsuites.test_weathere
import testsuites.test_applicai
import unittest
import getcwd

import HTMLTestRunnerCN
from framework.my_email import mail


if __name__ == "__main__":
    #创建一个suite集合
    suite = unittest.TestSuite()
    #将cese加进suite
    suite.addTest(testsuites.test_baidu.test_baidu('test_baisu'))
    suite.addTest(testsuites.test_baidu_new.test_baidu_new('test_new'))
    suite.addTest(requestsuites.test_weathere.weathere('test_weather'))
    suite.addTest(testsuites.test_applicai.test_licai('test_licai'))
    #生成报告
    path = getcwd.get_cwd()
    file_path = os.path.join(path, 'report/钱东敏测试自动化框架报告.html')
    fp = open(file_path, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='测试自动化框架报告',
        description='这个是一个示例报告',
        tester='数小钱'
    )
    runner.run(suite)
    fp.close()
    mail()