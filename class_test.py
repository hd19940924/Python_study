# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/20 16:20
# @filename :class_test.py
# 开发工具 ：PyCharm
class student():
    native_place="hefei"
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):

        print('%s: %s' % (self.name, self.score))

        print( (self.name, self.score))
    def eat(self):
        print("学生在吃饭")
    @staticmethod
    def drink():
        print("喝水")
    @classmethod
    def sleep(cls):
        print("睡觉了")
bart = student('Bart Simpson', 59)
bart.print_score()
#kk=student()
bart.eat()
bart.drink()
bart.sleep()
print(bart.name)
print(id(bart))
print(bart)
print(type(bart))
student.eat(bart)
print(student.native_place)
print(bart.native_place)
student.native_place="beijing"
print(bart.native_place)
print(student.native_place)