# encoding:utf-8
import logging

#设置日志的格式和输出文件名
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='lgy_log.log',
                    filemode='w')

#记录函数的执行信息，如时间，日期，作者等
def write_log(func,level=1):
    def wrap(*args,**kwargs):
        import time
        func(*args, **kwargs)
        logging.info("日志级别"+str(level)+'函数：'+time.strftime("%Y-%m-%d %H:%M:%S"))

    return wrap

#记录
def use_time(func):
    def wrap(*args, **kwargs):
        import time
        func(*args, **kwargs)
        now = time.clock()
        logging.info('函数执行时间：' + str(time.clock()-now))

    return wrap