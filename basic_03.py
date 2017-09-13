"""
面向对象的程序设计：
继承
鸭子类型
"""

import time

class Hero():
    '''
    这是一个超级英雄
    '''
    def __init__(self,name='zhangsan'):
        self.age = 30
        self.name = name

        # 如何设置一个不能被外部访问的属性，如一个人的秘密
        self.__age = 100

        # 如何设置带有标识位的属性,但可以被外部访问
        self._age = 90


    def run(self):
        print('我开始跑了',self.name)


if __name__ == '__main__':
    lgy = Hero('林国样')

    # 如何打印类的相关说明
    print(lgy.__doc__)

    # 如何查看一个类的所有属性和方法
    print(dir(Hero))

    # 如何打印一个类实例的所有方法
    print(Hero.__dict__)

    lgy.run()

    # 如何按照格式，打印日期的结果
    print(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))