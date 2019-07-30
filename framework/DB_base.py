# -*- coding: UTF-8 -*-
import pymysql
from Config.config import Config
from logs.log import log1


class DBbase:
    def __init__(self):

        # 连接数据库
        try:
            self.connect = pymysql.Connect(
                host='43.254.106.50',
                port=3306 ,
                user='uat' ,
                passwd='QsWc9v*%B5a#e' ,
                db='jbp_uat2' ,
            )
            # 获取游标
            self.cursor = self.connect.cursor()
        except:
            raise Exception("DataBase connect error,please check the db config.")

    def close(self):
        # 关闭查询
        self.cursor.close()

    def query(self, elemt,table):
        '''查询数据并返回
            cursor 为连接光标
            sql_str为查询语句
        '''
        try:
            sql='select {0} from {1}'.format(elemt, table)
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows
        except:
            return False

