# coding:utf-8
'''
此案例，用于测试鸭子类型的用法
'''

#人类
class Person(object):

    #交流的方法
    def communicate(self):
        print '我们是伟大的人类，可以交流信息'


#猴子
class Mokey(object):

    #交流的方法
    def communicate(self):
        print '我们是伟大的猴子，也可以交流信息'

#交流
def talking(animal):
    animal.communicate()

if __name__ == '__main__':

    #定义1个实例化的人，定义1各实例化的猴子
    one_person = Person()
    one_mokey = Mokey()

    #调用统一的方法：talking
    talking(one_person)
    talking(one_mokey)



