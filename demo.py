# coding:utf-8


class Person(object):
    '''这是一个测试函数'''

    #类属性
    meaning = "keep movint"

    #初始化这个类
    def __init__(self):
        self.a = 10
        self.b = 20
        self.mode = 'calm'
        self.__innerAtrr = 1000

    #定义一个功能
    def sexing(self):
        self.mode = 'exited'

    #定义一个说话功能
    def talking(self,content):
        self.a = 30
        print self.__innerAtrr
        for item in content:
            print item

    def print_a(self):
        # pass
        print 'abcd\n',
        print '\rcde'

lgy = Person()
lgy.talking([2,'bppp'])
lgy.meaning = 5

# print lgy.__dict__
lgy.print_a()

