__author__ = 'zn'
import pymysql
import logging
from Common import myLogger2



class my_sql:

    def __init__(self,conf_path):
        import configparser
        self.cf=configparser.ConfigParser() #实例化用configparser模块下的configParser类
        self.cf.read(conf_path)    #读取配置数据
        self.host=self.cf.get("mysql_info","host")
        self.user=self.cf.get("mysql_info","username")
        self.passwd=self.cf.get("mysql_info","password")
        self.db=self.cf.get("mysql_info","db")
        self.port=self.cf.getint("mysql_info","port")



    #连接数据库
    def connect_mysql(self):
        try:
            self.conn=pymysql.Connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,
                         port=self.port,charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            logging.info("数据库连接成功！！")
        except Exception as e:
            logging.exception("数据库连接失败原因为：%s",e)
            raise e
        self.cursor=self.conn.cursor()  # 使用cursor()方法获取操作游标

    #查询数据
    def select_info(self,sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except:
            self.conn.rollback()  #报错就回滚

    #关闭数据库
    def conn_close(self):
        self.conn.close()     #关闭数据库
        self.cursor.close()   #关闭游标
        logging.info("关闭数据库成功")


