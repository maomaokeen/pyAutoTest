import unittest
import requests
from logs.log import log1
import json
import os
import getcwd
import time

#如果使用https请求时，可以使用verify = false参数来跳过SLL证书认证，发布到生产的代码都应该加上timeout参数
class test_requests(unittest.TestCase):
    def get(self, url, params=None, headers=None, files=None):
        '''封装get方法，return响应码和相应内容'''
        try:
            r = requests.get(url, params=params, headers=headers, files=files)
            log1.info("请求的内容：%s" % params)
            status_code = r.status_code  # 获取返回的状态码
            log1.info("获取返回的状态码:%d" % status_code)
            response_json = r.json()  # 响应内容，json类型转化成python数据类型
            log1.info("响应内容：%s" % response_json)
            reurl = r.url  # 获取返回的状态码
            log1.info("url为:%s" % reurl)
            return status_code, response_json, reurl
        except BaseException as e:
            log1.error("请求失败！", exc_info=1)

    def post(self, url, data=None, headers=None,files=None):
        '''封装post请求，return响应码和响应内容'''
        try:
            r = requests.post(url, data=data, headers=headers, files=files)
            log1.info("请求的内容：%s" % data)
            status_code = r.status_code  # 获取返回的状态码
            log1.info("获取返回的状态码:%d" % status_code)
            response_json = r.json()  # 响应内容，json类型转化成python数据类型
            log1.info("响应内容：%s" % response_json)
            return status_code, response_json  # 返回响应码，响应内容
        except BaseException as e:
            log1.error("请求失败！", exc_info=1)

    def post_json(self, url,data=None,headers=None):
        '''封装post方法，并用json格式传值，return响应码和响应内容'''
        try:
            data = json.dumps(data).encode('utf-8')  # python数据类型转化为json数据类型
            r = requests.post(url, data=data, headers=headers)
            log1.info("请求的内容：%s" % data)
            status_code = r.status_code  # 获取返回的状态码
            log1.info("获取返回的状态码:%d" % status_code)
            response = r.json()  # 响应内容，json类型转化成python数据类型
            log1.info("响应内容：%s" % response)
            return status_code, response  # 返回响应码，响应内容
        except BaseException as e:
            log1.error("请求失败！", exc_info=1)

    def getdict(self, dict1, obj, default=None):
        ''' 遍历嵌套字典，得到想要的value
            dict1所需遍历的字典
            obj 所需value的键'''
        for k, v in dict1.items():
            if k == obj:
                return v
            else:
                if type(v) is dict:  # 如果是字典
                    re = self.getdict(v, obj, default)  # 递归
                    if re is not default:
                        return re
