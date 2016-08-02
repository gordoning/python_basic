#!/usr/bin/env python
# coding:utf-8
'''
@author:lgy
created by: 2016-06-18
'''

import urllib
from urllib.request import urlretrieve
import logging
import re
import time
import os

# 设置url/user_agent等信息
spider_url = "http://www.maiziedu.com/course/276-2604/"
spider_user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
spider_header = {"User-Agent":spider_user_agent}
spider_request = urllib.request.Request(headers=spider_header,url=spider_url)
spider_response = urllib.request.urlopen(spider_request)
spider_content = spider_response.read()
print(spider_content)

#做一个文件的编码转换
spider_content = spider_content.decode('utf-8')

# 分析网页内容
spider_regex = re.compile('<li class=".*?">.*?<a href="(.*?)" class="font14 color66">.*?<span class="col_l">(.*?)</span><span class="col_r color99">.*?</span>.*?</a>.*?</li>',re.S)
spider_items = re.findall(spider_regex,spider_content)

for s in spider_items:
    spider_path = 'lgy_spider/video'

    if not os.path.exists(spider_path):
        os.makedirs(spider_path)
    print(str(s))

    course_video_url = "http://www.maiziedu.com" + str(s[0])





