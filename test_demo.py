# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/21 15:48
# @filename :test_demo.py
# 开发工具 ：PyCharm
class Student():
    def __init__(self,name,age):
        self.name=name
        #self._age=age
        self.age=age
        print(name,age)
    def eat(self):
        print("吃饭")
    def get_age(self):
        #(self._age)
        print(self.age)
    def info(self):
        print("姓名：{0}，年纪：{1}".format(self.name,self.age))
    @classmethod
    def drink(cls):
        print("喝水")
    @staticmethod
    def sleep():
        print("睡觉了")
class stu_A(Student):
    def __init__(self, name, age,score):
        super().__init__(name,age)
        self.score=score
    def info(self):
        super().info()
        print("成绩：{0}".format(self.score))

stu2=stu_A("gg",19,99)
stu2.info()
stu=Student("张珊",13)
print(stu.name)
stu.get_age()
stu.info()
class middle_school_student(Student):
    pass

cc=middle_school_student(name="zhangsan",age=99)
cc.get_age()
print(dir(stu2))
print(id(stu2))
print(stu2.__dict__)
print(stu2.__class__)
print(stu2.__doc__)