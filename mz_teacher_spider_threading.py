#!/usr/bin/env python
#coding:utf-8
'''
Created on 2015年12月22日

@author: yopoing
'''
from __future__ import print_function

try:
    import urllib2
    import urllib
    from urllib2 import URLError as URLError
    from urllib2 import HTTPError as HTTPError
    from urllib import urlretrieve
    range = xrange
except ImportError:
    import urllib.request as urllib2
    from urllib.error import URLError as URLError
    from urllib.error import HTTPError as HTTPError
    from urllib.parse import quote
    from urllib.request import urlretrieve
import re
import os
import socket
import logging
import sys
import threading

# 获取python版本
python_version = sys.version_info[0]

# 设置超时时间
socket.setdefaulttimeout(30)

# 设置日志级别、格式和日期时间
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='mz_teacher_spider.log',
                filemode='w')

# 创建锁
spider_lock = threading.Lock()

def spider_run(pageIndex):
    print(threading.current_thread().name+u'正在保存第'+str(pageIndex)+u'页')
    url = 'http://www.maiziedu.com/course/teachers/?page='+str(pageIndex)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'
    headers = {'User-Agent': user_agent}
    content = ""
    try:
        # 设置request对象，里面包含访问的地址和头部信息
        request = urllib2.Request(url=url, headers=headers)
        # 为避免网络访问缓慢问题导致程序运行设置超时时间
        response = urllib2.urlopen(request, timeout=10)
        content = response.read() if python_version == 2 else response.read().decode('utf-8')
    except URLError as e:
        # 写异常日志
        logging.info('该地址不能访问('+str(e)+')：'+url)
    except HTTPError as e:
        # 写异常日志
        logging.info('该地址访问出错('+str(e)+')：'+url)
    except socket.timeout:
        # 写异常日志
        logging.info('该地址访问超时：'+url)
    
    # 通过正则表达式去分析获取想要提取的数据
    regex = re.compile('<li class="t3out">.*?<img.*?src="(.*?)">.*?<p class="font20 color00 marginB14 t3out p">(.*?)<a.*?<p class="color66">.*?</span>(.*?)</p>.*?</div>.*?</li>', re.S)
    items = re.findall(regex, content)
    
    # 保存到文件&保存头像
    save_path = 'teachers'
    save_str = ''
    avatar_path = 'teachers/avatar/'
    # 如果目录不存在，则创建对应的目录
    if not os.path.exists(save_path):
        # 注意是makedirs，不是mkdir方法，后者只能创建单个目录
        os.makedirs(save_path)
    if not os.path.exists(avatar_path):
        os.makedirs(avatar_path)
    for item in items:
        save_str += item[1]+'\n'+item[2]+'\n'
        # 保存头像
        file_path = item[0] if python_version == 2 else quote(item[0])
        avatar_url = 'http://www.maiziedu.com'+file_path
        print(threading.current_thread().name+' saving:'+avatar_url)
        avatar_name = item[0].split('/')[-1]
        try:
            path = unicode(avatar_path+avatar_name, 'utf-8') if python_version == 2 else avatar_path+avatar_name
            urlretrieve(avatar_url, path)
        except socket.timeout:
            logging.info('该文件下载超时：'+avatar_url)
            continue
    # 上锁
    spider_lock.acquire()
    with open(save_path+'/data.txt', 'a') if python_version==2 else open(save_path+'/data.txt', 'a', encoding='utf-8') as f:
        f.write(save_str)
    # 释放锁
    spider_lock.release()

if __name__ == '__main__':
    print(u'开始抓取...')
    # 抓取20个页面，从1开始
    t_list = []
    for i in range(1, 26):
        t = threading.Thread(target=spider_run, args=(i,))
        t_list.append(t)
        t.start()
    for t in t_list:
        t.join()
    print(u'抓取结束...')

