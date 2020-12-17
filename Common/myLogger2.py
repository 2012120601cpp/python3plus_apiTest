#Author:
import logging
from logging.handlers import RotatingFileHandler
import time
from Common import myConfig as C

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

#输出到控制台
handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())

#输出到文件
handler_2 = RotatingFileHandler(C.logs_dir+"/Api_Autotest_log_{0}.log".format(curTime),backupCount=20,encoding='utf-8')

logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])

logging.info("=========test start=========")

