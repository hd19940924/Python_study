# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/21 15:21
# @filename :class_demo.py
# 开发工具 ：PyCharm
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(name,age)
    def eat(self):
        print("吃饭")
    @classmethod
    def drink(cls):
        print("喝水")
    @staticmethod
    def sleep():
        print("睡觉了")
Student.drink()
Student.sleep()
#Student.eat() 错误写法
#stu1=Student()
stu1=Student(name="bb",age=89)
stu1.eat()
def show():
    print("我是类外函数")
stu1.show=show()
stu1.show