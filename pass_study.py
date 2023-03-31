# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/20 16:36
# @filename :pass_study.py
# 开发工具 ：PyCharm
class Student:
    pass
bb=Student()
bb.name="hh"
print(bb.name)
a=20
b=10
#c=a+b
c=a.__add__(b)
print(c)
l=[1,2,3.4,5,6]
print(l.__len__())