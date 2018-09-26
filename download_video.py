"""
下载b站的小视频
"""

import requests,os

if __name__ == '__main__':

    # 设置头文件信息
    header = {"User-Agent":'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'}

    # 下载地址的信息
    download_url = 'http://upos-hz-mirrorks3.acgvideo.com/dspxcode/i180926tx26aqdcpdt7q8c2pmfjho49h-1-56.mp4?um_deadline=1537940383&rate=500000&oi=987110627&um_sign=ed2fffcc63cd9187707444f098bd18ec&gen=dsp&wsTime=1537940383&platform=html5'

    # 设置视频存储的地址
    save_path = '/Users/lgy/Downloads/'

    # 下载文件
    response = requests.get(download_url,headers=header)


    print(response.status_code)

    # 将文件存储到文件夹中
    if response.status_code == 200:
        with open(os.path.join(save_path, "abc.mp4"), 'wb') as file:
            file.write(response.content)

