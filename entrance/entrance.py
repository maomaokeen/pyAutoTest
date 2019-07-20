# -*- coding: UTF-8 -*-
import testsuites.test_baidu
import testsuites.test_baidu_new
import requestsuites.test_weathere
import unittest
import getcwd
import os
import HTMLTestRunnerCN
from framework.my_email import mail


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testsuites.test_baidu.test_baidu('test_baisu'))
    suite.addTest(testsuites.test_baidu_new.test_baidu_new('test_new'))
    suite.addTest(requestsuites.test_weathere.weathere('test_weather'))
    suite2 = unittest.TestSuite()
    suite2.addTest(testsuites.test_baidu_new.test_baidu_new('test_new'))
    path = getcwd.get_cwd()
    file_path = os.path.join(path, 'report/钱东敏测试自动化框架报告.html')
    fp = open(file_path, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='钱东敏测试自动化框架报告',
        description='报告中描述部分',
        tester='数小钱'
    )
    runner.run(suite)
    runner.run(suite2)
    fp.close()
    mail()