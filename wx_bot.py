__auth__ = 'linguoyang'
__date__ = '2018/9/5 下午6:41'

from wxpy import *

bot = Bot()

yyy = bot.friends().search('点点点')[0]

yyy.send('测试一下')

tuling = Tuling(api_key='efb99df6a75b40e0abd3a064ee5e3dec')

# 使用图灵机器人自动与指定好友聊天
@bot.register(yyy)
def reply_my_friend(msg):
    tuling.do_reply(msg)

embed()