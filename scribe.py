# coding:utf-8
'''
订阅模式
项目介绍：
彩票开奖功能，点击开始，系统就会自动开奖
开奖规则是这样的：6个红球和1个篮球（红球范围1-33；蓝球范围1-16）
'''

import random
import time

#球类
class Ball(object):
    def __init__(self):
        self.color = ''
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

    counts = 200

    def __init__(self, red_ball, blue_ball):

        #初始化开奖小球
        self.red_ball_list = [red_ball()] * 6
        self.blue_ball = blue_ball()

        self._time = "2016-06-26"

        #保存开奖结果
        self.red_ball_numbers = []
        self.blue_ball_number = 0

        self.observers = []

    #正式开奖
    def run(self):

        #开球计数
        count = 0
        #开奖：红色球
        for ball in self.red_ball_list:
            ball.run()
            count =count + 1
            print('开了第%d个红球'%count)
            # print "开红球："+str(ball.number)+"   "
            self.red_ball_numbers.append(ball.number)
            time.sleep(0.3)

        #开奖：蓝色球
        self.blue_ball.run()
        print('开了第1个蓝球')
        # print "开蓝球：" + str(self.blue_ball.number)
        self.blue_ball_number = self.blue_ball.number

        #通知所有显示器，显示开奖结果
        print("\n>>开奖结束,马上通知所有的显示器\n\n")
        time.sleep(1)
        self.notify_observers()

    #注册一个观察者
    def register_observer(self,display):
        self.observers.append(display)

    #删除一个观察者
    def remove_observer(self, display):
        self.observers.remove(display)

    #通知显示器,兰球和红色球的结果
    def notify_observers(self):
        #开奖的结果，通知
        dict_number = {'red_ball_numbers':self.red_ball_numbers,'blue_ball_number':self.blue_ball_number}
        for observer in self.observers:
            observer.update(dict_number)

    @staticmethod
    def self_killing():
        print('i am over,88%s'%lottery_Machine.counts)

    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls,'_instance'):
    #         cls._instance = super(lottery_Machine,cls).__new__(cls,*args,**kwargs)
    #     return cls._instance

#LED看板，显示结果
class LED_Display():
    def __init__(self,lottery_machine=None):
        self.lottery_machine = lottery_machine
        self.lottery_machine.register_observer(self)
        self.red_ball_list = []
        self.blue_ball = 0

    #获取开奖结果：6个红球，1个兰球
    #同时立马显示出来
    def update(self,dict_number):
        self.red_ball_list = dict_number['red_ball_numbers']
        self.blue_ball = dict_number['blue_ball_number']
        self.displaying()

    #显示结果
    def displaying(self):

        print('！！！!!这是LED显示器')

        for bull_number in self.red_ball_list:
            print('LED红:'+str(bull_number) + '  ')

        print('LED蓝:'+str(self.blue_ball))


#PC显示器上的看板
#LED看板，显示结果
class PC_Display():
    def __init__(self,lottery_machine=None):
        self.lottery_machine = lottery_machine
        self.lottery_machine.register_observer(self)
        self.red_ball_list = []
        self.blue_ball = 0

    #获取开奖结果：6个红球，1个兰球
    #同时立马显示出来
    def update(self,dict_number):
        self.red_ball_list = dict_number['red_ball_numbers']
        self.blue_ball = dict_number['blue_ball_number']
        self.displaying()

    #显示结果
    def displaying(self):

        print('\n#####这是PC显示器：')

        for bull_number in self.red_ball_list:
            print('PC红:'+str(bull_number) + '  ')
        print('PC蓝:'+str(self.blue_ball))

if __name__ == '__main__':
    lottery_machine = lottery_Machine(red_Ball,blue_Ball)
    lottery_machine2 = lottery_Machine(red_Ball, blue_Ball)
    #定义两个不同的显示器，分别接受开奖机的开奖结果，自动显示出来
    led_display = LED_Display(lottery_machine)
    pc_display = PC_Display(lottery_machine2)

    lottery_machine.self_killing()

    lottery_machine.run()
    lottery_machine2.run()

    print(lottery_machine._time)





