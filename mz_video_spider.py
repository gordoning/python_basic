#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function

import sys
try:
    reload(sys)  
    sys.setdefaultencoding('utf8')
    import urllib2
    from urllib import urlretrieve
except (ImportError, NameError):
    import urllib.request as urllib2
    from urllib.request import urlretrieve
import re
import os
import logging
import time

# 获取python版本
python_version = sys.version_info[0]

class RateLimit(object): 

    """限制下载速度""" 

    def __init__(self, rate_limit): 

        """限制速率单位 KB/s""" 
        self.rate_limit = rate_limit 
        self.start = time.time() 

    def __call__(self, block_count, block_size, total_size): 
        # 总大小(KB)
        total_kb = total_size / 1024
        # 已下载(KB)
        downloaded_kb = (block_count * block_size) / 1024
        # 实际消耗时间(s)
        elapsed_time = time.time() - self.start 
        if elapsed_time != 0: 
            # 实际下载速度
            rate = downloaded_kb / elapsed_time 
            # 剩余倒计时
            count_down = int((total_kb - downloaded_kb) / rate) if rate>0 else 0
            # 下载进度
            par = 100.0 * block_count * block_size/ total_size
            if block_count * block_size <= total_size:
                print(u'\r进度：%.2f%%，速度：%.1fkB/s, 总大小：%dKB, 已下载：%dKB, 倒计时：%ds \r' % (par, rate, total_kb, downloaded_kb, count_down), end='')
            # 限制速率情况下的下载时间（期望时间）
            expected_time = downloaded_kb / self.rate_limit 
            # 计算睡眠时间 = 期望时间 - 实际消耗时间
            sleep_time = expected_time - elapsed_time 
            # 让程序处于睡眠状态以达到限速的目的
            if sleep_time > 0: 
                time.sleep(sleep_time) 

if __name__ == '__main__':  #程序入口
    #抓取视频，并且保存到本地maizi/vedio文件夹
    # 这段代码思路有些问题，正确的思路应该是你先根据目标地址，把30个视频的播放地址获取到放到之后，再挨个根据这30个地址去获取网页内容，
    # 然后提取里面的视频真正地址，然后再进行保存，所以最外层的那个循环其实都是不需要的。各位同学可以尝试修改完善改程序。
    # 目标地址
    spurl = 'http://www.maiziedu.com/course/python/425-5465/'
    # 头部信息         
    spuser_anget = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    sppattern = re.compile('''<source src="(.*?)" type='video/mp4' />''',re.S)
    spdows = re.compile('<li class=".*?">.*?<a href="(.*?)" class="font14 color66">.*?<span class="col_l">(.*?)</span><span class="col_r color99">.*?</span>.*?</a>.*?</li>',re.S)
    spheaders = {'User-Anget':spuser_anget}
    sprequest = urllib2.Request(url = spurl,headers = spheaders)
    spresponse = urllib2.urlopen(sprequest)
    spcontent = spresponse.read()
    spcontent = spcontent if sys.version_info[0] == 2 else spcontent.decode('utf-8')
    spurl_items = re.findall(spdows,spcontent) #获取视频播放网页
    for s in spurl_items:
        sppath = 'maizi/video'
        if not os.path.exists(sppath):
            os.makedirs(sppath)
        i = 'http://www.maiziedu.com' + str(s[0])
        sppage = urllib2.urlopen(i)
        sppagec = sppage.read()
        sppagec = sppagec if sys.version_info[0] == 2 else sppagec.decode('utf-8')
        spvideo_items = re.findall(sppattern,sppagec) #获取视频
        for q in spvideo_items:
            print(u'当前正在下载：'+q)
            spdow = sppath + '/' + str(s[1]) + '.' + 'm4v'
            spdow = spdow if python_version == 3 else unicode(spdow,'utf-8')
            # 使用urlretrieve下载视频，使用钩子函数计算下载进度
            urlretrieve(q, spdow, RateLimit(100))
#                 spop = urllib2.urlopen(q)
#                 spdownload = spop.read()
#                 with open(unicode(spdow,'utf-8'),'wb') as dow:
#                     dow.write(spdownload)