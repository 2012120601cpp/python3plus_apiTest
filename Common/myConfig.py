__author__ = 'zn'
import os

# 目录配置
# os.path.split作用：把文件目录和文件名分离出来，返回一个元组
# os.path.abspath作用：获取当前代码路径，无论把这个模块复制在哪里，都只获取当前放置该模块所在的路径
# __file__作用：内置变量不能随便使用更改
# [0]作用：获取返回元组的第一个值
cur_dir = os.path.split(os.path.abspath(__file__))[0]

testcase_dir = cur_dir.replace("Common","Testdatas")

htmlreport_dir = cur_dir.replace("Common","HtmlTestReport")

logs_dir = cur_dir.replace("Common","Logs")

mysql_path=cur_dir+"/mysqlConnInfoConf.conf"

excel_path=cur_dir.replace("Common","Testdatas")+"/APi_autotest.xlsx"