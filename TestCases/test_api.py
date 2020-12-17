__author__ = 'zn'
import unittest
import logging
import ddt
from Common.Doexcel import DoExcel
from Common import myConfig as C
from Common import myDubbo_conn
from Common.myMysql import my_sql
from Common import myLogger2
import re
import time

# 实例化exccel类获取所有的测试数据
excelfile = C.testcase_dir + "/APi_autotest.xlsx"
de = DoExcel(excelfile)
all_case_datas = de.getAllCaseDatas()
logging.info("所有的测试数据为：%s", all_case_datas)


@ddt.ddt
class Test_api(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        de.update_init_data()
        de.save_excel(C.excel_path)
        # #连接数据库
        self.mysql = my_sql(C.mysql_path)  # 实例化
        self.mysql.connect_mysql()  # 连接数据库

    @ddt.data(*all_case_datas)
    # 传入请求参数发起请求
    def test_api(self, case_data):
        logging.info("================开始发送一次接口请求，请求信息如下===========")
        logging.info("接口请求apiName：%s", case_data["api_name"])
        logging.info("接口请求interface:%s", case_data["interface"])
        logging.info("接口请求method:%s", case_data["method"])
        logging.info("接口请求data:%s", case_data["request_data"])
        # logging.info("接口请求sql:%s",case_data["execute_sql"])

        try:
            res = myDubbo_conn.dubbo_request(case_data["ip"], case_data["port"], case_data["interface"],
                                             case_data["method"], case_data["request_data"])
        except Exception as e:
            logging.exception("接口请求失败原因为:%s", e)
            raise e
        logging.info("接口请求response data为：%s", res)
        logging.info("接口请求expected data为:%s", case_data["expected_data"])

        # 开始校验期待结果与实际结果
        if case_data["compare_type"] != None:
            if int(case_data["compare_type"]) == 0:
                logging.info("=====开始比对检验返回结果=======")
                logging.info("全值匹配模式")
                try:
                    self.assertIn(str(res), case_data["expected_data"])
                    logging.info("结果比对成功，测试用例通过")
                except Exception as e:
                    logging.exception("全值结果比对失败原因为：%s", e)
                    raise e
            elif int(case_data["compare_type"]) == 1:
                logging.info("=====开始比对检验返回结果=======")
                logging.info("正则表达式匹配模式")
                try:
                    self.assertIsNotNone(re.search(case_data["expected_data"], str(res)))
                    logging.info("结果匹配，测试用例通过")
                except Exception as e:
                    logging.exception("正则结果比对失败原因为;%s", e)
                    raise e

        # 判断是否需要进行数据库验证
        if case_data["execute_sql"] != None:
            for i in eval(case_data["execute_sql"]):
                try:
                    res = self.mysql.select_info(i)
                    self.assertIsNotNone(res)
                    logging.info("数据库里存在符合预期条件的数据,测试通过:%s", res)
                except Exception as e:
                    print("数据库中不存在,验证失败原因为：%s", e)
        logging.info("================结束一次接口请求===========")

        # #判断接口发起请求后如果需要等待则设置等待时间
        if case_data["wait_time"] != None:
            logging.info("需要等待时间60s发起后续请求")
            time.sleep(60)
