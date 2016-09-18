# coding: utf-8
import threading
import time

def hello():
    print "lgy"
    time.sleep(1)
    print threading.current_thread().name

if __name__ == '__main__':
    start = time.clock()
    thread_list = []
    for i in range(1,3):
        t = threading.Thread(target=hello)
        thread_list.append(t)
        t.start()

    for t in thread_list:
        print "开始了"
        t.join()

    end = time.clock()
    print threading.current_thread().name
    print '花掉时间'+str(end-start)