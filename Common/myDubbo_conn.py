__author__ = 'zn'
import dubbo_telnet
from Common import myConfig as C
#import requests
#import json
#dubbo接口请求
def dubbo_request(host,port,interface,method,param=None):

         #初始化dubbo对象
         conn = dubbo_telnet.connect(host,port)
         #设置telnet连接超时时间
         conn.set_connect_timeout(10)
         #设置dubbo服务返回响应的编码
         conn.set_encoding('gbk')
         if param != None:
             #把jason字符串转成字典
             param=eval(param)
         if param == '':
            param=param
         command='invoke %s.%s(%s)'%(interface,method,param)
         res=conn.do(command)
         return res


#http接口请求
# def my_requests(url,method,request_data):
#     if method =="get":
#         res=requests.get(url,params=request_data)
#         requests.request()
#     elif method =="post":
#         res=requests.post(url,data=request_data)
#     else:
#         res=None
#     return res.text