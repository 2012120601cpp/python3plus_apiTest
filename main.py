__author__ = 'zn'
import unittest
from TestCases import test_api
from Common import myConfig
import time
from Common import HTMLTestRunner

# 读取test开头文件里的测试数据加入到testloader中，测试结果写入到html中
s = unittest.TestSuite()
ul = unittest.TestLoader()
s.addTests(ul.loadTestsFromModule(test_api))
curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
fp = open(myConfig.htmlreport_dir + '/API_autoTest_{0}.html'.format(curTime), 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='WutongApiTestReport',
    description='WutongApiTestReport',
    tester="ZhouNuo",
    verbosity=2
)
runner.run(s)
