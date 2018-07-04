from splinter.browser import Browser
import time
from PIL import ImageGrab
'''
使用splinter操作网页
'''

if __name__ =='__main__':
    # browser=Browser('chrome', headless=True)


    browser=Browser('chrome')
    browser.visit("http://wx.zhinengxiyifang.cn/admin/index.html#!/franchiseeManager")
    # button_1 = browser.find_by_id('su')
    time.sleep(5)
    browser.find_by_id('J_Quick2Static').click()
    browser.fill('TPL_username','linguoyang2008')
    browser.fill('TPL_password','123456wolf')
    browser.find_by_id('J_SubmitStatic').click()
    time.sleep(5)



    if browser.is_text_present('知乎'):
        print("找到你了")

    # browser.driver.close()

    # 获取当前所有窗口handle列表，这个文档里面有

    # 列表里面的窗口按打开顺序排列

    # allwindows = browser.windows
    #
    # # 切换到刚开的窗口
    #
    # browser.driver.switch_to_window(allwindows[-1])
    #
    # # 关闭当前窗口
    #
    # browser.driver.close()
    # im = ImageGrab.grab()
    # im.save('lgy_screen','RGB')


    try:
        time.sleep(60)
    except KeyboardInterrupt:
        print("被中断了")
        browser.quit()