#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2016/2/17
@author: yopoing
功能描述
"""
# 方案一：
# 直接print,可复用性很差，其他地方无法复用该函数
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print b
#         a, b = b, a + b
#         n = n + 1
#
# fab(5)

# 方案二（改进）：将生成的数列放到列表里面
# 在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List
# def fab(max):
#     n, a, b = 0, 0, 1
#     num_list = []
#     while n < max:
#         num_list.append(b)
#         a, b = b, a + b
#         n = n + 1
#     return num_list
#
# for i in fab(5):
#     print i

# 方案三（使用迭代器）:
# 使用 class 改写的这个版本，代码远远没有第一版的 fab 函数来得简洁。如果我们想要保持第一版 fab 函数的简洁性，同时又要获得 iterable 的效果，yield 就派上用场了
# class Fab(object):
#     def __init__(self, max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.n < self.max:
#             tmp = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n = self.n + 1
#             return tmp
#         raise StopIteration()

# 方案四（使用生成器）：
# 第四个版本的 fab 和第一版相比，仅仅把 print b 改为了 yield b，就在保持简洁性的同时获得了 iterable 的效果
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

# def test(len):
#     i = 0
#     while i < len:
#         yield i
#         i += 1
#
# t = test(5)
# print t.next()

def consumer():
    n = 0
    print '消费者初始化'
    while True:
        n = yield n
        if not n:
            return
        n -= 1
        print '消费了1，还剩余%d'%n

def produce(c):
    n = 0
    next(c)
    while n < 6:
        n += 2
        print '生产了2，总共有%d'%n
        n = c.send(n)
        print '确认还剩：%d'%n
    c.close()

consumer()
consumer()
# c = consumer()
# produce(c)

# for i in fab(10000):
#     print i
# print type(fab(10))

