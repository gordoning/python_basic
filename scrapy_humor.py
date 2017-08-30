"""
爬取糗事百科的最新信息
"""
import re
import requests
import os

if __name__ == '__main__':
    response = requests.get('https://www.qiushibaike.com/text/')
    content = response.content
    regex = re.compile('<div class="content">(.*?)</span>',re.S)
    items = re.findall(regex,content.decode('utf-8'))
    path_dir = "humor"
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    i = 0
    for item in items:
        i = i+1
        print(item)
        file_path = path_dir + '/' + str(i) + '.txt'
        content_new = item.replace(' ','').replace('<span>','').replace('<br/>','')
        with open(file_path,'w') as f:
            f.write(content_new)

