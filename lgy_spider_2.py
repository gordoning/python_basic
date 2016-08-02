#!/usr/bin/env python
#coding:utf-8
'''
Created on 2015年12月22日

@author: yopoing
'''
import urllib2
import urllib
import re
import os
import socket
import logging

# 设置超时时间
socket.setdefaulttimeout(30)

# 设置日志级别、格式和日期时间
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='mz_teacher_spider.log',
                filemode='w')

print '开始抓取...'
# 抓取20个页面，从1开始
for i in xrange(1,21):
    print '正在保存第'+str(i)+'页'
    url = 'http://www.1mai1ziedu.com/course/teachers/?page='+str(i)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'
    headers = {'User-Agent': user_agent}
    try:
        # 设置request对象，里面包含访问的地址和头部信息
        request = urllib2.Request(url=url, headers=headers)
        # 为避免网络访问缓慢问题导致程序运行设置超时时间
        response = urllib2.urlopen(request, timeout=3)
        content = response.read()
    except urllib2.URLError as e:
        # 写异常日志
        logging.info('该地址不能访问('+str(e)+')：'+url)
        continue
    except urllib2.HTTPError as e:
        # 写异常日志
        logging.info('该地址访问出错('+str(e)+')：'+url)
        continue
    except socket.timeout:
        # 写异常日志
        logging.info('该地址访问超时：'+url)
        continue
    
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
        avatar_url = 'http://www.maiziedu.com'+item[0]
        print '正在保存：'+avatar_url
        avatar_name = item[0].split('/')[-1]
        try:
            urllib.urlretrieve(avatar_url, unicode(avatar_path+avatar_name, 'utf-8'))
        except socket.timeout:
            logging.info('该文件下载超时：'+avatar_url)
            continue
    with open(save_path+'/data.txt', 'a') as f:
        f.write(save_str)
print '抓取结束...'

