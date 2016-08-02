# encoding:utf-8

from lgy_decorator import use_time
from lgy_decorator import write_log

#测试函数
@use_time
@write_log
def hello_world(name="傻逼"):
    print name + ":正在测试装饰器的使用方法"

hello_world()