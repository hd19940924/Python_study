# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/22 15:07
# @filename :duojicheng_test.py
# 开发工具 ：PyCharm
class Person(object):
    def eat(self):
        print("人会使用工具吃饭")
class man():
    def run(self):
        print("男人跑的更快")
class Student(Person,man):
    def run(self):
        super().run()
        print("hhhhh")

     #pass
stu=Student()
stu.run()
stu.eat()