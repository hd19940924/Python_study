# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/2/22 10:30
# @filename :dynamic_test.py
# 开发工具 ：PyCharm
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    #pass

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
   # pass

    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Eating meat...')
class EE():
    def run(self):
        print('EE is running...')
dog = Dog()
dog.run()

cat = Cat()
cat.run()
def fun(animal):
    animal.run()
fun(Dog())
fun(Cat())
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(EE())
