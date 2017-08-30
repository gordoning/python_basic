#coding:utf-8
"""
python的基础知识_01
列表 元组 集合等
"""


# 如何把字符串，组合成一句自定义的话？
str = "{0},is a good {1}".format("linguoyang","man")

# 元组如果只有1个元素，如何表达？
tuple2 = (1,)


#如何声明一个数组
list1 = list()

# 如何判断一个序列是空的
if not list1:
    print("列表是空的")

# 如何声明一个元组
tuple1 = tuple()

# 如何声明一个空的字典
dict1 = {}

dict1['name'] = 'linguoyang'
dict1['age'] = 12

# 列表的相加
list1 = list1 + ["linguoyang","zhangsan","李光辉","李蛋蛋"]

# 如何将一个字符串的字符全部提取出来？
list2 = [i for i in str]

# 如何声明一个集合
set1 = set()

# 如何添加元素到一个集合？2种方式？
set1.add('lgy')
set1.update('china')

# 如何从一个集合中，删除一个元素？
set1.remove('c')

# 如何判断一个元素，是否在集合中？
tt = 'a' in set1

# 如何计算两个集合的交集，并集，差集
sset1 = set1&set2
sset2 = set1|set2
sset3 = set1-set2

# 如何让列表的元素进行倒序,倒数后3个？考虑下步长
list3=list1[-1:-4:-1]

# 指数运算怎么做，比如2的5次方？
result = 2**5

# 除法之后，舍掉小数点，怎么做？
abc = 9//2

# 模块和包的区别在什么地方？
# 模块就是一个.py的文件
# 包是包含了一个__init__.py的文件夹，可以被import
from mypack import module
# print(module.name2)

# 如何快速查看一个函数的使用方法
import time,os
dir(time)

# 如何生成一个1到200的序列
list4 = range(1,200,2)

# 如何定义一个可变参数的函数
def myprint(*task):
    print(task)

myprint(12,'linguoyang','章三')

# 如何定义一个关键字参数的函数
def myprint2(**kwargs):
    print(kwargs)

# myprint2(name="王三", age=88)


# 文件操作的3大核心流程是什么？
"""
1，打开文件；2，写入内容；3，关闭程序
懂了吗？
"""
onefile = open('guoyang.txt','w')
onefile.write("通畅财务自由，从python开始")
onefile.close()

# 如何用一句代码就完成文件操作的3大核心流程呢？
with open('guoyang.txt','r+') as twofile:
    print(twofile.read())

# 捕获异常的标准处理格式是怎样的？
# 捕获异常的好处是什么？
# 答：不影响后边程序的顺利执行
try:
    print(int(4.4))
except ValueError as e:
    print('捕获到以下的异常:',e)
else:
    print("没有任何异常")
finally:
    print("不管怎样，我都执行一下")

print("程序到此结束")


# 如何触发一个异常
# raise ValueError

# 如何用一句代码，来表示判断语句的逻辑处理？
a = 3 if False else 1
# print(a)