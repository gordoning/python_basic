# coding:utf-8
'''
双色球：
点击【开始】
6个红球和1个篮球（红球范围1-33；蓝球范围1-16）
'''

import random
import time

#球类
class Ball(object):
    def __init__(self):
        self.number = 0

#红球
class red_Ball(Ball):
    def __init__(self):
        self.color = 'red'

    def run(self):
        self.number = random.randint(1,33)

#蓝球
class blue_Ball(Ball):
    def __init__(self):
        self.color = 'blue'

    def run(self):
        self.number = random.randint(1,16)

#开奖机
class lottery_Machine(object):
    def __init__(self, red_ball, blue_ball):
        self.red_ball_list = [red_ball()] * 6
        self.blue_ball = blue_ball()
        self.all_ball = {'red_bulls': [0] * 6, 'bule_ball': 0}

    #正式开奖
    def run(self):
        result_file = open('result'+time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),'w')

        #开奖：红色球
        result_file.write("\n红色球：")
        for ball in self.red_ball_list:
            ball.run()
            print "开红球："+str(ball.number)+"   两秒后开始下一个球..."
            time.sleep(2)
            result_file.write(str(ball.number)+'   ')

        #开奖：蓝色球
        result_file.write("\n蓝色球：")
        self.blue_ball.run()
        print "开蓝球：" + str(self.blue_ball.number)
        result_file.write(str(self.blue_ball.number)+'   ')

        if result_file.close():
           print "开奖结束"

if __name__ == '__main__':
    current_game = lottery_Machine(red_Ball,blue_Ball)
    current_game.run()

